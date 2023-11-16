# Tulip
This file contains everything needed to know in order to have an understanding about `DF`.

## Requirements
- `docker` (Engine & CLI)
    - `compose` (Tool)
    
The only tool needed to get `DF` working is `docker` along with its `compose` tool.

## Configurations
`DF` uses a file (`config.py`) and **environment variables**.

### services/api/configurations.py
Edit this file by editing the following variables:
    1.  `FLAG_FORMAT` - flag regex
    2.  `TEAMS` - Dictionary enemyTeamName:IP
    3.  `SYSTEM_PROTOCOL` - you can create your own protocol but it's discouraged
    4.  `SYSTEM_HOST` - IP of the game server
    5.  `SYSTEM_PORT` - Port of the game server
    6.  `TEAM_TOKEN` - team token
    7.  `SUBMIT_FLAG_LIMIT`
    8.  `SUBMIT_PERIOD` - time to wait between a sending session
    9.  `FLAG_LIFETIME`
    

## Running

    ## DF HOST ONLY

    run container with
        -`docker compose up --build -d`

    ## NON HOST

    connect directly to `http://<HOST>:5000` so you can access the web-interface
        Username: None
        Password: `VvP0Uxw6JFyUeDQe`


###### HOW TO EXPLOIT ######

1. Check for vulnerabilities on enemy teams' services

2. Write a .py script to test the exploit on your own.
#### IMPORTANT: DO NOT DEPLOY AN UNTESTED SCRIPT

3. Open run_sploit.py; You DO NOT need to change anything but the following:
    - Insert your code inside the loop function. DO NOT erase the content

4. Run run_sploit.py; You should be all right.

5. Repeat these steps everytime you find another possible exploit

## References
Tulip GitHub Repository - https://github.com/OpenAttackDefenseTools/tulip