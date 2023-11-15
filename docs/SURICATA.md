This file contains everything needed to know in order to have an understanding about `Suricata`.
## Install
1. `apt install suricata`
### Requirements
immense

## Config

1. in `/etc/suricata/suricata.yaml` sostitiusci `- suricata.rules` a riga 1862 con il path delle tue regole `- /ctf/ipsrules/local.rules`

2. crea il path delle regole `/ctf/ipsrules/local.rules` e aggiungine almeno una
	#example: 
	```
	alert tcp $HOME_NET 1984 -> $EXTERNAL_NET any (msg: "Path Traversal-../"; content: "../"; metadata: tag path_traversal; sid:1; rev: 1;)
	alert tcp any any -> any any (msg: "Path Global-../"; flow:to_server; content: "../"; metadata: tag path_traversal; sid:2; rev: 2;)
	```
3. add **iptables rules** for the NFQUEUE with IP and Port (add both input and output rules):
	example where $ip = localhost; $dp = 1984;
	`sudo iptables -I INPUT -d "$ip" -p tcp --dport "$dp" -j NFQUEUE --queue-num 1 --queue-bypass`
	`sudo iptables -I OUTPUT -d "$ip" -p tcp --dport "$dp" -j NFQUEUE --queue-num 1 --queue-bypass`
	>you can also add a rule in --sport but its usefulness is still in test phase
	>
4. inizia il processo tramite screen 
	`sudo screen -dmS surica suricata -c /etc/suricata/suricata.yaml -q 0`	
	 

## Usage

### start and restart to modify rules, change settings

Use command `screen -r surica` and ctrl-c to close the process, then modify file `local.rules` and execute `sudo screen -dmS surica suricata -c /etc/suricata/suricata.yaml -q 0` again
p.s. don't use `systemctl`

### rule writing
example
`alert tcp $HOME_NET 1337 -> $EXTERNAL_NET 1337 (msg: "Path Traversal-../"; content: "../"; metadata: tag path_traversal; sid:1; rev: 1;)`

content:
-
- for ascii characters "../"
- for hex characters "yes|A0||13||37|normal|fe|"
- [every type of rules](https://docs.suricata.io/en/suricata-6.0.0/rules/payload-keywords.html#content) (startswith, regex , ...)
also
- msg is shown in /var/log/suricata/fast.log 
- metadata: tag is shown in Tulip 
- alert produces an alert, drop drops the packet
- IMPORTANT: change sid and rev every new rule or conflict will happen


## Files for debugging
- **/etc/suricata/suricata.yaml** -> 1900 line configs (search keywords in nano with crtl-w), just change the rule line 1862 with your path and you'll be ok, nfqueue permits us to not set anything else
- **/var/log/suricata/suricata.log** -> logs errors of rule and config loading in each startup
- **/var/log/suricata/fast.log** -> logs real-time positive alerts and drops with the msg and other fields
- **/etc/suricata/rules** -> useless, default rules
- **/var/log/suricata/eve.json** -> contains json of every little data. it is used by tulip. **TODO**: comment '#' protocols in `suricata.yaml` file in section `eve.json` and use that suricata.yaml instaed
