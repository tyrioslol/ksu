# this script protects against useradds
# intrusion logs for users are stored in /var/log/intrusions/users

# screwup check
while [ True ]
do
    echo "!! IMPORTANT !!"
    echo "have you removed all unwanted users? (y/n)"
    read ans
    if [ $ans == "y" ]
    then
        break
    elif [ $ans == "n" ]
    then
        echo "please remove unwanted users first..."
        echo "potential users with shells -"
        grep "bash|sh|dash|zsh|ksh|csh|tcsh" /etc/passwd
        exit 1
    else
        continue
    fi
done

# create for pass
mkdir /var/log/intrusions
touch /var/log/intrusions/users
chmod 500 /var/log/intrusions/users
touch /opt/pass_back
cat /etc/passwd > /opt/pass_back
chmod 400 /opt/pass_back
cat /etc/passwd | cut -d ":" -f 1 > /opt/auth_users
chmod 400 /opt/auth_users

# create for shadow
touch /var/log/intrusions/shadows
chmod 500 /var/log/intrusions/shadows
touch /opt/shadow_back
cat /etc/shadow > /opt/shadow_back
chmod 400 /opt/shadow_back
cat /etc/shadow | cut -d ":" -f 1 > /opt/auth_shadows

# move to opt
cp grooper.sh /opt/brady.sh
chmod 400 /opt/brady.sh
chmod +x /opt/brady.sh

# make the cronjob
touch /tmp/cron_hold
crontab -l > /tmp/cron_hold
echo "* * * * * /opt/brady.sh" >> /tmp/cron_hold
crontab /tmp/cron_hold
rm /tmp/cron_hold
