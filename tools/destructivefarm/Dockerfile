FROM alpine:latest

WORKDIR /destructivefarm

#: Get dependencies
RUN apk add --no-cache git python3 py3-pip

#: Clone DestructiveFarm repo
RUN git clone https://github.com/DestructiveVoice/DestructiveFarm.git .

#: Install python dependencies inside server/requirements.txt
RUN pip3 install -r server/requirements.txt

#: Overwrite server/config.py with our own
COPY config.py server/config.py

#: Add our protocols
COPY protocols/ server/protocols/

#: Run the server with server/start_server.sh
CMD ["sh", "server/start_server.sh"]