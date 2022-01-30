**Linux Cheatsheet:**

Set root password:
```
!!!!IMPORTANT!!!!
DO THIS FIRST:
  1. su root
  2. passwd
  3. set new password 
```

Wazuh Server:
```
curl -so ~/unattended-installation.sh https://packages.wazuh.com/resources/4.2/open-distro/unattended-installation/unattended-installation.sh && bash ~/unattended-installation.sh
```

Wazuh Agent:
```
APT-
  
  Install the agent:
  
  $ curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | apt-key add -
  $ echo "deb https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/wazuh.list
  $ apt-get update
  $ WAZUH_MANAGER="10.0.0.2" apt-get install wazuh-agent
  $ /var/ossec/bin/agent-auth -m <manager_IP>
  
  Registering the agent:
  
  $ /var/ossec/bin/agent-auth -m <manager_IP>
  $ nano /var/ossec/etc/ossec.conf
  <client>
    <server>
      <address>MANAGER_IP</address>
    </server>
  </client>
  $ systemctl restart wazuh-agent
  
  install/enable auditd:
  
  $ sudo apt-get install audit
  $ nano /var/ossec/etc/ossec.conf
  ## Add this near the end of the config file. You can just copy and paste from one of the others to make it easier.
  <localfile>
   <log_format>audit</log_format>
   <location>/var/log/audit/audit.log</location>
  </localfile>
  
  Monitor directories:
  
  $ auditctl -w /home -p w -k audit-wazuh-w
  $ auditctl -w /etc -p w -k audit-wazuh-w
  $ auditctl -w /usr -p w -k audit-wazuh-w
  $ auditctl -w /bin -p w -k audit-wazuh-w
  $ auditctl -w /tmp -p w -k audit-wazuh-w
  $ auditctl -w /sbin -p w -k audit-wazuh-w
  $ auditctl -w /opt -p w -k audit-wazuh-w
  $ auditctl -w /boot -p w -k audit-wazuh-w
  
  Monitor command execution by user with admin privs:

  $ auditctl -a exit,always -F euid=0 -F arch=b64 -S execve -k audit-wazuh-c
  $ auditctl -a exit,always -F euid=0 -F arch=b32 -S execve -k audit-wazuh-c
```
```
Yum-
  
  Install the agent:
  
  $ rpm --import https://packages.wazuh.com/key/GPG-KEY-WAZUH
  $ cat > /etc/yum.repos.d/wazuh.repo << EOF
  [wazuh]
  gpgcheck=1
  gpgkey=https://packages.wazuh.com/key/GPG-KEY-WAZUH
  enabled=1
  name=EL-\$releasever - Wazuh
  baseurl=https://packages.wazuh.com/4.x/yum/
  protect=1
  EOF
  $ WAZUH_MANAGER="10.0.0.2" yum install wazuh-agent
  
  Registering the agent:
  
  $ /var/ossec/bin/agent-auth -m <manager_IP>
  $ nano /var/ossec/etc/ossec.conf
  <client>
    <server>
      <address>MANAGER_IP</address>
    </server>
  </client>
  $ systemctl restart wazuh-agent
  
  install/enable auditd:
  
  $ sudo yum install auditd
  $ nano /var/ossec/etc/ossec.conf
  ## Add this near the end of the config file. You can just copy and paste from one of the others to make it easier.
  <localfile>
   <log_format>audit</log_format>
   <location>/var/log/audit/audit.log</location>
  </localfile>
  
  Monitor directories:
  
  $ auditctl -w /home -p w -k audit-wazuh-w
  $ auditctl -w /etc -p w -k audit-wazuh-w
  $ auditctl -w /usr -p w -k audit-wazuh-w
  $ auditctl -w /bin -p w -k audit-wazuh-w
  $ auditctl -w /tmp -p w -k audit-wazuh-w
  $ auditctl -w /sbin -p w -k audit-wazuh-w
  $ auditctl -w /opt -p w -k audit-wazuh-w
  $ auditctl -w /boot -p w -k audit-wazuh-w
  
  Monitor command execution by user with admin privs:

  $ auditctl -a exit,always -F euid=0 -F arch=b64 -S execve -k audit-wazuh-c
  $ auditctl -a exit,always -F euid=0 -F arch=b32 -S execve -k audit-wazuh-c
```

Update:
```
sudo apt-get update && sudo apt-get upgrade -y
sudo yum update
```

Change MySQL Root Password:
```
mysql -u root -p
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('supersecurepassword');
FLUSH PRIVILEGES;
```

Show Users: 
```
cat /etc/passwd
cat /etc/passwd | grep /bin/bash && cat /etc/passwd | grep /bin/sh
```

Delete Users: 
```
sudo userdel username / sudo deluser username
```

Show Groups:
```
cat /etc/group
cat /etc/group | grep sudo && cat /etc/group | grep admin
```

Remove Users from Group:
2 Methods:
```
sudo gpasswd -d username group
sudo nano /etc/group
```

Install nmap:
```
sudo apt-get install net-tools
sudo apt install nmap
sudo yum install nmap
```

Use nmap to enumerate services:
```
nmap -sT -sV 127.0.0.1 > services.txt
nmap -p- 127.0.0.1 (run in background) > allports.txt
```

UDP scan: 
```
nmap -sU localhost
```

Verify and Identify Service:
```
sudo netstat -tulpn | grep LISTEN
```

Kill Process:
```
sudo killall process_name
sudo kill processid
```

Configure SSH:
```
nano /etc/ssh/sshd_config
permitrootlogin no
# Consider changing to key based authentication
```
Stop SSH:
```
sudo service sshd stop
sudo service sshd status
# OR
sudo systemctl stop sshd
sudo systemctl status sshd
```
