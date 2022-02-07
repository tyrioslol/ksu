thisdiff=$(which diff)
thisgrep=$(which grep | grep bin | xargs)
thiscut=$(which cut)
thisuserdel=$(which userdel)

"$thisdiff" /etc/passwd /opt/pass_back > /var/log/intrusions/users
for i in $("$thisgrep" ":" /var/log/intrusions/users | "$thiscut" -d ":" -f 1 | "$thiscut" -d " " -f 2)
do 
    if grep -wFxq "$i" /opt/auth_users
    then
        continue
    else
        "$thisuserdel" $i
    fi
done

"$thisdiff" /etc/shadow /opt/shadow_back > /var/log/intrusions/shadows
for i in $("$thisgrep" ":" /var/log/intrusions/shadows | "$thiscut" -d ":" -f 1 | "$thiscut" -d " " -f 2)
do 
    if grep -wFxq "$i" /opt/auth_shadows
    then
        continue
    else
        "$thisuserdel" $i
    fi
done
