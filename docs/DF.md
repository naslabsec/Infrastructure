###### HOST ONLY ######

1. Check the options in config.py:
    1. IP enemy vulnbox
    2. Flag regex
    3. `FLAG_LIFETIME`
    4. `SUBMIT_PERIOD`
    5. `TEAM_TOKEN`

2. Check ccit protocol script for the following:
    1. RESPONSES: change according to given rules (Row 6)
 
3. run container with
    -`docker compose up --build -d`


###### NON HOST ONLY ######

1. connect directly to `http://<HOST>:5000` so you can access the web-interface
    Username: None
    Password: `VvP0Uxw6JFyUeDQe`

###### HOW TO EXPLOIT ######

1. Check for vulnerabilities on enemy teams' services

2. Write a .py script to test the exploit on your own.
#### IMPORTANT: DO NOT DEPLOY AN UNTESTED SCRIPT

3. Open run_sploit.py; You DO NOT need to change anything but the following:
    - Insert your code inside the loop function. DO NOT erase the content
    
    ### HOW TO USE FLAG_IDS
    This script is a one-4-all. It means that it should be able to handle all kind of payload.
    If you do not want to use the FlagIDS, just type 0 when requested. Otherwise, choose the service you want to exploit.

    Before try and attempting to write a script, you should check manually the /flagIds. It will give you information about the json.

    `flag_ids` is a list made from a json where you can find all the content of the /flagIds. To access the content of it, you should use it as a dictionary. For example: `flag_ids['poll_id']` if you want to access the field `poll_id` and so on. For further explaination look for json structure or contact <Th3R0ck>

4. Run run_sploit.py; You should be all right.

5. Repeat these steps everytime you find another possible exploit
