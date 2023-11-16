FROM alpine:latest

ARG MACHINE_IP
ARG MACHINE_PASSWORD

#: Ensure SSH utils
RUN apk add --no-cache openssh sshpass

#: Install Ansible along with dependencies
RUN apk add --no-cache python3 py3-pip ansible

#: Generate SSH key ed25519
RUN ssh-keygen -q -t ed25519 -N "" -C "Generated by Ansible Dockerfile" -f /root/.ssh/id_ed25519

#: Add SSH key to authorized_keys to allow Ansible to connect to MACHINE_IP
RUN sshpass -p ${MACHINE_PASSWORD} ssh-copy-id -o StrictHostKeyChecking=no -i /root/.ssh/id_ed25519.pub root@${MACHINE_IP}

ENTRYPOINT ["tail", "-f", "/dev/null"]