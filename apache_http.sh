#!/bin/bash
# make this file executable with chmod +x before running

yum install httpd httpd-manual nano -y
touch /var/www/html/page.html
echo "Access Denied. Contact Administrators." >> /var/www/html/page.html
cd /etc/httpd/conf.d/
wget https://raw.githubusercontent.com/JCam6/DefensiveSecurity/main/Bash/site1.conf
systemctl enable httpd.service
systemctl start httpd.service
firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --add-port=80/tcp
cp /var/www/html/page.html /var/www/html/index.html
exit

# open web browser at http://<machineIPaddress>/page.html
# update web page scripts at /var/www/html/*.html
# update config file at /etc/httpd/conf.d/site1.conf