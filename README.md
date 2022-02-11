# ksu
This repo contains various scripts for use in CCDC. 

clone this repo with:
```
git clone https://github.com/tyrioslol/ksu.git
```

Usage:
```bash
cd prevent
chmod +x user_protect.sh
./user_protect.sh
```
```bash
cd wazuh
chmod +x wazuh_agent.sh
./wazuh_agent.sh
```

Cheat Sheet:
```
# backup /etc
tar -czvf /tmp/etc.tar.gz /etc; mv /tmp/etc.tar.gz /opt; chmod 400 /opt/etc.tar.gz; chattr +i /opt/etc.tar.gz

# backup /var
tar -czvf /tmp/var.tar.gz /var; mv /tmp/var.tar.gz /opt; chmod 400 /opt/var.tar.gz; chattr +i /opt/var.tar.gz

# backup /<whatever>
tar -czvf /tmp/<whatever>.tar.gz /<whatever>; mv /tmp/<whatever>.tar.gz /opt; chmod 400 /opt/<whatever>.tar.gz; chattr +i /opt/<whatever>.tar.gz

# SQL stuff
mysql -u root -p
select User, Host from mysql.user;
DROP 'testaccount'@'localhost'
show processlist;
KILL Id_number;
```
