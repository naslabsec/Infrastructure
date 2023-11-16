# Suricata
Suricata is a high performance, open source network analysis and threat detection software

## Requirements
`apt install suricata`

## Configurations
With the following steps you can install Suricata and get the right config to start using it quick-start.

1. in File: `/etc/suricata/suricata.yaml` go to line 1862 and substitute `- suricata.rules` with `- /ctf/ipsrules/local.rules`

2. Create rules file `/ctf/ipsrules/local.rules` add at least one rule [How to write rules](https://docs.suricata.io/en/suricata-6.0.0/rules/intro.html)

	#example: 
	```
	alert tcp $HOME_NET 1984 -> $EXTERNAL_NET any (msg: "Path Traversal-../"; content: "../"; metadata: tag path_traversal; sid:1; rev: 1;)
	alert tcp any any -> any any (msg: "Path Global-../"; flow:to_server; content: "../"; metadata: tag path_traversal; sid:2; rev: 2;)
	```

3. !IMPORTANT! Set-up **iptables rules** that sends pkts to NFQUEUE. Write the rules exactly like this with right IP and Port (add both input and output rules):
	```bash
	ip = "localhost"
	dp = "1337"
	sudo iptables -I INPUT -d "$ip" -p tcp --dport "$dp" -j NFQUEUE --queue-num 1 --queue-bypass
	sudo iptables -I OUTPUT -d "$ip" -p tcp --sport "$dp" -j NFQUEUE --queue-num 1 --queue-bypass
	```
	
1. Start Suricata in [IPS mode](https://suricata.readthedocs.io/en/suricata-6.0.0/setting-up-ipsinline-for-linux.html) using screen
	`sudo screen -dmS surica suricata -c /etc/suricata/suricata.yaml -q 0`	

## Usage
### start and restart

Start Suricata in [IPS mode](https://suricata.readthedocs.io/en/suricata-6.0.0/setting-up-ipsinline-for-linux.html) using screen:
`sudo screen -dmS surica suricata -c /etc/suricata/suricata.yaml -q 0`	

Restart Suricata after modifying rules or config:
`screen -r surica` and ctrl-c to close the process

### rule writing
example
`alert tcp $HOME_NET 1337 -> $EXTERNAL_NET 1337 (msg: "Path Traversal-../"; content: "../"; metadata: tag path_traversal; sid:1; rev: 1;)`

rules content match:
- ascii characters "abcd1234../"
- hex characters "yes|A0||13||37|normal|fe|"
- [different rules from content](https://docs.suricata.io/en/suricata-6.0.0/rules/payload-keywords.html#content) (startswith, regex , ...)

other fields in rules:
- msg is displayed in /var/log/suricata/fast.log
- metadata: the tag is shown in Tulip 
- alert produces an alert, drop drops the packet  (see them in `/var/log/suricata/fast.log`)
- IMPORTANT: change sid and rev every new rule or conflict will happen


## Useful Files for debugging
- **/etc/suricata/suricata.yaml** -> 1900 line configs (search keywords in nano with crtl-w), just change the rule line 1862 with your path and you'll be ok, nfqueue permits us to not set anything else
- **/var/log/suricata/suricata.log** -> logs errors of rule and config loading in each startup
- **/var/log/suricata/fast.log** -> logs real-time positive alerts and drops with the msg and other fields
- **/etc/suricata/rules** -> useless, default rules
- **/var/log/suricata/eve.json** -> contains json of every little data. it is used by tulip. **TODO**: comment '#' each protocol in `suricata.yaml` file that in section `eve.json` gets the file too big


## References
https://suricata.readthedocs.io
