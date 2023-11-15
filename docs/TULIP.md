# Tulip
This file contains everything needed to know in order to have an understanding about `Tulip`.

## Requirements
- `docker` (Engine & CLI)
    - `compose` (Tool)
    
The only tool needed to get `Tulip` working is `docker` along with its `compose` tool.

## Configurations
`Tulip` uses a file (`services/api/configurations.py`) and **environment variables**.

### services/api/configurations.py
Edit this file by creating the following variables:
A `str` called `vm_ip` with your **VulnBox IP**.

A `list` called `services`.
This `list` should contain a `dict` for each service, each `dict` should have 3 keys: 
- `ip`
- `port`
- `name`

#### Example
```python
vm_ip = "10.10.23.1"
services = [
    { "port": 8080, "name": "http_sqli" }
]
for service in services:
    services["ip"] = vm_ip
```

### Environment Variables
- `FLAG_REGEX` -> The **regex** of the **flag** (e.g. `[A-Z0-9]{31}=`)
- `TULIP_MONGO` -> **IP** and **PORT** of MongoDB (since it's in a docker container you can just use the default value of `mongo:27017`).
- `TRAFFIC_DIR_HOST` -> The <ins>**host**</ins> **directory** (*without* trailing slash) where `Tulip` reads the `.pcap` files. (e.g. `/var/log/pcaps`).
- `TRAFFIC_DIR_DOCKER` -> The <ins>**containter**</ins> **directory** (*without* trailing slash) where `Tulip` reads the `.pcap` files. (e.g. `/traffic`).
- `TICK_START` -> An **ISO 8601** date representing when the CTF started (`YYYY-MM-DDTHH:MM+HH:MM`) (e.g. `2023-11-18T18:00+01:00`, means 18 november 2023 at 18:00 with +1 timezone, if it was UTC timezone it would be at 17:00).
- `TICK_LENGTH` -> **Frequency** of ticks. (e.g. 18000 means a tick **every 18000 ms**)

## Running on the vulnbox
Assuming that you, the team member, have `docker` (and `compose`) installed on your own machine and that you are **online** (you are connected to the Internet); you could do the following:
1. Install `Tulip` on your machine, configuring it with the right parameters.
2. Meanwhile install `Docker` with the [static binaries](https://docs.docker.com/engine/install/binaries/#install-daemon-and-client-binaries-on-linux) on the vulnbox.
3. When `Tulip` is done installing on your machine, you can **save** the various images using the [`docker save`](https://docs.docker.com/engine/reference/commandline/save/) command and then **transfer them** to the vulnbox.
4. After transferring the various images, ***restore*** them using the [`docker load`](https://docs.docker.com/engine/reference/commandline/load/) command.
5. Now you can just launch the `docker-compose up` command, since you already have the images available Docker won't try to pull them from the registry. (check [this](https://stackoverflow.com/questions/20481225/how-can-i-use-a-local-image-as-the-base-image-with-a-dockerfile) out).

## References
Tulip GitHub Repository - https://github.com/OpenAttackDefenseTools/tulip
