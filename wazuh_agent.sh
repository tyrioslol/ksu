## Wazuh Install Script

echo "enter wazuh server IP:"
read manager_ip

echo "name this host:"
read hostname

while [ true ]
do
    echo "enter package manager (yum/apt)"
    read package_manager
    if [ $package_manager != 'apt' ] && [ $package_manager != 'yum' ]
    then
        echo "must be apt or yum"
        continue
    else
        if [ $package_manager == 'apt' ]
        then

            # install agent and register to server
            apt-get install apt-transport-https nano gnupg gnupg2 gnupg1 -y
            curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | apt-key add -
            echo "deb https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/wazuh.list
            apt-get update
            WAZUH_MANAGER=$manager_ip apt-get install wazuh-agent -y
            /var/ossec/bin/agent-auth -m $manager_ip -A $hostname

            # validate agent config
            echo "valdate the manager ip in the config. 
            should be $manager_ip"
            read -p "Press enter to continue"
            nano /var/ossec/etc/ossec.conf

            # do audit stuff
            apt-get install auditd -y
            apt-get install audit -y
            echo "copy this and add at line 209:
  <localfile>
    <log_format>audit</log_format>
    <location>/var/log/audit/audit.log</location>
  </localfile>"
            read -p "Press enter to continue"
            nano /var/ossec/etc/ossec.conf

            # audit stuff : watching directories
            auditctl -w /home -p w -k audit-wazuh-w
            auditctl -w /etc -p w -k audit-wazuh-w
            auditctl -w /usr -p w -k audit-wazuh-w
            auditctl -w /bin -p w -k audit-wazuh-w
            auditctl -w /tmp -p w -k audit-wazuh-w
            auditctl -w /sbin -p w -k audit-wazuh-w
            auditctl -w /opt -p w -k audit-wazuh-w
            auditctl -w /boot -p w -k audit-wazuh-w

            # audit stuff : watching command execution
            auditctl -a exit,always -F euid=0 -F arch=b64 -S execve -k audit-wazuh-c
            auditctl -a exit,always -F euid=0 -F arch=b64 -S execve -k audit-wazuh-c

            # restart the agent
            systemctl restart wazuh-agent

            break
        else

            # install agent and register to server
            yum update -y
            yum install nano -y
            rpm --import https://packages.wazuh.com/key/GPG-KEY-WAZUH
            
            wazuh_key="[wazuh]
gpgcheck=1
gpgkey=https://packages.wazuh.com/key/GPG-KEY-WAZUH
enabled=1
name=EL-\$releasever - Wazuh
baseurl=https://packages.wazuh.com/4.x/yum/
protect=1"
            echo "$wazuh_key" > /etc/yum.repos.d/wazuh.repo

            WAZUH_MANAGER=$manager_ip yum install wazuh-agent
            /var/ossec/bin/agent-auth -m $manager_ip -A $hostname

            # validate agent config
            echo "valdate the manager ip in the config. 
            should be $manager_ip"
            read -p "Press enter to continue"
            nano /var/ossec/etc/ossec.conf

            # do audit stuff
            yum install auditd -y
            yum install audit -y
            echo "copy this and add at line 209:
  <localfile>
    <log_format>audit</log_format>
    <location>/var/log/audit/audit.log</location>
  </localfile>"
            read -p "Press enter to continue"
            nano /var/ossec/etc/ossec.conf

            # audit stuff : watching directories
            auditctl -w /home -p w -k audit-wazuh-w
            auditctl -w /etc -p w -k audit-wazuh-w
            auditctl -w /usr -p w -k audit-wazuh-w
            auditctl -w /bin -p w -k audit-wazuh-w
            auditctl -w /tmp -p w -k audit-wazuh-w
            auditctl -w /sbin -p w -k audit-wazuh-w
            auditctl -w /opt -p w -k audit-wazuh-w
            auditctl -w /boot -p w -k audit-wazuh-w

            # audit stuff : watching command execution
            auditctl -a exit,always -F euid=0 -F arch=b64 -S execve -k audit-wazuh-c
            auditctl -a exit,always -F euid=0 -F arch=b64 -S execve -k audit-wazuh-c

            # restart the agent
            systemctl restart wazuh-agent

            break
        fi
    fi
done
