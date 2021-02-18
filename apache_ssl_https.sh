#!/bin/bash
yum install httpd httpd-manual openssl mod_ssl nano -y
systemctl restart httpd.service
firewall-cmd --permanent --add-service=https
firewall-cmd --permanent --add-port=443/tcp
firewall-cmd --reload
mkdir /etc/httpd/ssl
cd /etc/httpd/ssl
echo -e " This will generate the Apache SSL Certificate and Key!\nEnter the name of KSU for the files:"
read cert
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out $cert.key
chmod 600 $cert.key
openssl req -new -key $cert.key -out $cert.csr
openssl x509 -req -days 365 -in $cert.csr -signkey $cert.key -out $cert.crt
echo -e " The Certificate and Key files for $cert have been generated!\nPlease link it to Apache SSL available website!"
ls -all /etc/httpd/ssl
echo "Access Denied. Contact Administrators." >> /var/www/html/page2.html
cp /var/www/html/page2.html /var/www/html/index.html
cd /etc/httpd/conf.d/
wget https://raw.githubusercontent.com/JCam6/DefensiveSecurity/main/Bash/site2.conf
systemctl restart httpd.service
exit

# open web browser at http://<machineIPaddress>/page2.html
# update web page scripts at /var/www/html/*.html
# update config file at /etc/httpd/conf.d/site2.conf