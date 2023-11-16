"""
    DestructiveFarm-compatible protocol implementation (TCP)

    Consider the following checksystem:
    - one flag per line ending with `\n`
    - the server will respond with `[OK]` if the flag is valid
    - the server will respond with `[ERR]` if the flag is invalid
    - the server will respond with `[OFFLINE]` if the server is offline
"""
import socket

from server.models import FlagStatus, SubmitResult

RESPONSES = {
    FlagStatus.ACCEPTED: [
        "[OK]",
    ],
    FlagStatus.REJECTED: [
        "[ERR]",
    ],
    FlagStatus.SKIPPED: [
        "[OFFLINE]"
    ]
}

READ_TIMEOUT = 1
BUFFER_SIZE = 1024
APPEND_TIMEOUT = 0.05

def recvall(sock: socket.socket) -> bytes:
    """
        Receive all data from socket

        Args: 
            sock: socket to read from

        Returns:
            Data read from the socket
    """
    sock.settimeout(READ_TIMEOUT)
    chunks = [sock.recv(BUFFER_SIZE)]

    sock.settimeout(APPEND_TIMEOUT)
    while True:
        try:
            chunk = sock.recv(BUFFER_SIZE)
            if not chunk:
                break

            chunks.append(chunk)
        except socket.timeout:
            break

    sock.settimeout(READ_TIMEOUT)
    return b''.join(chunks)

def submit_flags(flags, config):
    """
        DestructiveFarm-compatible submit flags function
    """
    sock = socket.create_connection((config['SYSTEM_HOST'], config['SYSTEM_PORT']), READ_TIMEOUT)

    for item in flags:
        sock.sendall(item.flag.encode() + b'\n')
        response = recvall(sock).decode().strip()

        for status, substring in RESPONSES.items():
            if any(s in response for s in substring):
                found_status = status
                break
        else:
            found_status = FlagStatus.QUEUED

        yield SubmitResult(item.flag, found_status, response)

    sock.close()
