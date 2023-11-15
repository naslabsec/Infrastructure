## Install & config
1. install suricata, screen
2. put in nfq mode with queue-bypass queue-num 1 every port you want to monitor:
	example where $ip = localhost and $dp = 1984:
	`sudo iptables -I INPUT -d "$ip" -p tcp --dport "$dp" -j NFQUEUE --queue-num 1 --queue-bypass`
	`sudo iptables -I OUTPUT -d "$ip" -p tcp --dport "$dp" -j NFQUEUE --queue-num 1 --queue-bypass`

3. in `/etc/suricata/suricata.yaml` rimuovi suricata.rules a riga 1862 e metti il path delle tue regole /ctf/ipsrules/local.rules

4. crea il path delle regole e aggiungi almeno una regoletta
	example: `alert tcp any any -> any any (msg: "Path Traversal-../"; content: "../"; metadata: tag path_traversal; sid:1; rev: 1;)`

5. inizia il processo
	`sudo screen -dmS surica suricata -c /etc/suricata/suricata.yaml -q 0`	

## Usage

### start and restart

Use command `screen -r surica` and ctrl-c to close the process, then modify file `local.rules` and execute `sudo screen -dmS surica suricata -c /etc/suricata/suricata.yaml -q 0` again

p.s. don't use `systemctl`

### rule writing
example
`alert tcp any any -> any any (msg: "Path Traversal-../"; content: "../"; metadata: tag path_traversal; sid:1; rev: 1;)`

>content:
for ascii characters "../"
for hex characters "|A0||13||37|normal"



