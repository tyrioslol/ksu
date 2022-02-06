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
        echo "here are users with shells:"
        grep "bash|sh|dash|zsh|ksh|csh|tcsh" /etc/passwd
        exit 1
    else
        continue
    fi
done

# create files we need
mkdir /var/log/intrusions
touch /var/log/intrusions/users
chmod 500 /var/log/intrusions/users
touch /opt/pass_back
cat /etc/passwd > /opt/pass_back
chmod 400 /opt/pass_back
touch /opt/user_protect.sh
chmod 400 /opt/user_protect.sh
chmod +x /opt/user_protect.sh
thisdiff=$(which diff)
thisgrep=$(which grep | grep bin | xargs)
thiscut=$(which cut)
thisuserdel=$(which userdel)
echo ''$thisdiff' /etc/passwd /opt/pass_back > /var/log/intrusions/users; for i in $('$thisgrep' ":" /var/log/intrusions/users | '$thiscut' -d ":" -f 1 | '$thiscut' -d " " -f 2); do '$thisuserdel' $i; done' > /opt/user_protect.sh

# make the cronjob
touch /tmp/cron_hold
crontab -l > /tmp/cron_hold
echo "* * * * * /opt/user_protect.sh" >> /tmp/cron_hold
crontab /tmp/cron_hold
rm /tmp/cron_hold
