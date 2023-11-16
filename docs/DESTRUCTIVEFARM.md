# DestructiveFarm
This file explains the general workflow for using `DestructiveFarm` and how it should be configured.

## Overview
DestructiveFarm is composed by 3 **main components**:
1. An **exploit**: receives an **IP** as the first command-line argument and **writes** the **flag** on **`stdout`**.
2. A **client**: periodically runs an **exploit**, retrieves the flag from **`stdout`** and then sends it to the **server**.
3. A **server**: gets the **flags** from the **clients** and sends them to the **checksystem**.

## Requirements
- `docker`
    - `compose`
    
The only tool needed to get `DestructiveFarm` working is `docker` along with its `compose` tool.

## Configurations
The <ins>only</ins> configuration needed is the one of the **server**, `server/config.py`.

### server/config.py
The `server/config.py` is composed by one big `dict` named `CONFIG` having the following keys:
- `TEAMS` -> A `dict` with a **single key** (the team name, e.g. `Team #2`) having as value the **team IP**
- `FLAG_FORMAT` -> The **regex** matching the flag.
- `SYSTEM_PROTOCOL` -> Which **protocol** to use, should be the name of a **`.py` file** placed in `server/protocols`.
- `SYSTEM_HOST` -> The **IP** of the **DestructiveFarm server**.
- `SYSTEM_PORT` -> The **port** of the DestructiveFarm server**.
- `FLAG_LIFETIME` -> How long a flag **lasts** in **seconds**.
- `SUBMIT_PERIOD` -> **Frequency** of flag submissions in **seconds**.
- `SUBMIT_FLAG_LIMIT` -> How many **flags** can be **submitted** each `SUBMIT_PERIOD` **seconds**.
- `SERVER_PASSWORD` -> The **password** to access the **web interface**.

#### Example
```python
CONFIG = {
    'TEAMS': {'Team #{}'.format(i): '10.0.0.{}'.format(i)
              for i in range(1, 29 + 1)},
    'FLAG_FORMAT': r'[A-Z0-9]{31}=',
    'SYSTEM_PROTOCOL': 'tcp_protocol',
    'SYSTEM_HOST': '127.0.0.1',
    'SYSTEM_PORT': 31337,
    'SUBMIT_FLAG_LIMIT': 50,
    'SUBMIT_PERIOD': 5,
    'FLAG_LIFETIME': 5 * 60,
    'SERVER_PASSWORD': '0xdeadbeef',
}
```

## Running
`DestructiveFarm` is composed by **two parts**, the **client** and the **server**.

### Server
The server **must** not be run on the **VulnBox**, instead run it on one of the **team member computer**.

In order to start the server, run the **docker container** with
```
docker-compose up -d
```
Where the **`-d`** option is for **`detatch`**, so you *don't* hang your terminal for the container.

### Client
There can be **multiple** clients from the same host machine.
A client is **spawned** when the **`start_sploit.py` script** is **ran**.

In order to spawn one client, `start_sploit.py` must be called with the **right arguments**, which are:
- `your_exploit.py` -> The **first** argument that **must** be passed to `start_sploit.py`, the exploit will then get called with the **target machine IP** as the **first command-line argument** and **must** write the **flag** to **stdout**
- `-u` / `--server-url` -> The **URL** of the **DestructiveFarm** server (e.g. `http://10.10.42.49:5000`)

#### Exploit Example
```python
import sys
TARGET_MACHINE_IP = sys.argv[1]

def get_flag() -> str:
    ...
    
print(get_flag())
```

#### Client Example
```
python3 start_sploit.py exploit.py -u http://10.10.42.49:5000
```


## References
DestructiveFarm GitHub Repository - https://github.com/DestructiveVoice/DestructiveFarm
