import os
import sys

if not os.geteuid()==0:
    sys.exit('This script must be run as root!')

os.system("clear")

# Check DNS
print("Checking DNS Settings...")
os.system("cat /etc/resolv.conf | grep nameserver")

while True:
    print("\nWould you like to change your DNS server? (y/n)")
    ans = input()
    if ans == "y":
        print("Updating...")
        os.system("echo 'nameserver 8.8.8.8' > /etc/resolv.conf")
        break
    if ans == "n":
        print("Moving on...")
        break
    if ans != "y" or ans != "n":
        print("Invalid: Must be y/n")
        continue

os.system("clear")
input("Done: Press Enter to continue...")
os.system("clear")
    
# what os are you
while True:
    print("I'm a dumb script. What OS are you running on? (ubuntu/debian/centos/fedora)")
    ans = input()
    if ans == "fedora":
        print("Fedora selected.")
        _os = "cent"
        break
    if ans == "centos":
        print("CentOS selected.")
        _os = "cent"
        break
    if ans == "ubuntu":
        print("Ubuntu selected.")
        _os = "debian"
        break
    if ans == "debian":
        print("Debian selected.")
        _os = "debian"
        break
    if ans != "ubuntu" or ans != "debian" or ans != "centos" or ans != "fedora":
        print("Invalid: Must be ubuntu/debian/centos/fedora")
        continue

# update if you want
if _os == "debian": 
    while True:
        print("\nWould you like to update now? (y/n)")
        ans = input()
        if ans == "y":
            print("Updating...")
            os.system("apt-get update && apt-get upgrade -y")
            break
        if ans == "n":
            print("Moving on...")
            break
        if ans != "y" or ans != "n":
            print("Invalid: Must be y/n")
            continue
elif _os == "cent":
    while True:
        print("\nWould you like to update now? (y/n)")
        ans = input()
        if ans == "y":
            print("Updating...")
            os.system("sudo yum update")
            break
        if ans == "n":
            print("Moving on...")
            break
        if ans != "y" or ans != "n":
            print("Invalid: Must be y/n")
            continue

if _os == "debian":
    # Install git
    print("\nInstalling git...")
    os.system("apt-get install git -y | 2>/dev/null")
    print("Done")
    os.system("which git")

    # Install wget
    print("\nInstalling wget...")
    os.system("apt-get install wget -y | 2>/dev/null")
    print("Done")
    os.system("which wget")

    # Install python3
    print("\nInstalling python...")
    os.system("apt-get install python3 -y | 2>/dev/null")
    print("Done")
    os.system("which python3")

    # Install UFW
    print("\nInstalling UFW...")
    os.system("apt-get install ufw -y | 2>/dev/null")
    print("Done")
    os.system("which ufw")

    # Installing nmap
    print("\nInstalling nmap...")
    os.system("apt-get install nmap -y | 2>/dev/null")
    print("Done")
    os.system("which nmap")
    print("\nScanning...")
    os.system("nmap -sT -sV localhost > scan.txt")
    print("Done, results saved to scan.txt.")

    # Install netstat/nettools
    print("\nInstalling net-tools/netstat...")
    os.system("apt-get install net-tools | 2>/dev/null")
    print("Done")
    os.system("which netstat")
    os.system("netstat -tulpn | grep LISTEN > netstat.txt")
    print("Done, results saved to netstat.txt.")

    # Installing fail2ban
    print("\nInstalling fail2ban...")
    os.system("apt-get install fail2ban -y | 2>/dev/null")
    print("Done")
    os.system("fail2ban-client status")

    # Importing linpeas
    # print("\nGetting linpeas and running local scan...")
    # os.system("wget https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh && chmod +x linpeas.sh | 2>/dev/null")

if _os == "cent":
    # Install git
    print("\nInstalling git...")
    os.system("yum install git | 2>/dev/null")
    print("Done")
    os.system("which git")

    # Install wget
    print("\nInstalling wget...")
    os.system("yum install wget | 2>/dev/null")
    print("Done")
    os.system("which wget")

    # Install python3
    print("\nInstalling python...")
    os.system("yum install python3 | 2>/dev/null")
    print("Done")
    os.system("which python3")

    # Installing nmap
    print("\nInstalling nmap...")
    os.system("yum install nmap | 2>/dev/null")
    print("Done")
    os.system("which nmap")
    print("\nScanning...")
    os.system("nmap -sT -sV localhost > scan.txt")
    print("Done, results saved to scan.txt.")

    # Install netstat/nettools
    print("\nInstalling net-tools/netstat...")
    os.system("yum install net-tools | 2>/dev/null")
    print("Done")
    os.system("which netstat")
    os.system("netstat -tulpn | grep LISTEN > netstat.txt")
    print("Done, results saved to netstat.txt.")

    # Installing fail2ban
    print("\nInstalling fail2ban...")
    os.system("yum install fail2ban | 2>/dev/null")
    print("Done")
    os.system("fail2ban-client status")

    # Importing linpeas
    # print("\nGetting linpeas and running local scan...")
    # os.system("wget https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh && chmod +x linpeas.sh | 2>/dev/null")

#while True:
#    print("\nWould you like to run linpeas now? (y/n)")
#    ans = input()
#    if ans == "y":
#        print("INFO: linpeas is present on your system.\nSimply su into another user and run the script with ./linpeas.sh.")
#        print("Done")
#        break
#    if ans == "n":
#        print("Moving on...")
#        break
#    if ans != "y" or ans != "n":
#        print("Invalid: Must be y/n")
#        continue
        
while True:
    print("\nIt's recommended to reboot after updating. Would you like to reboot now? (y/n)")
    ans = input()
    if ans == "y":
        os.system("reboot")
        break
    if ans == "n":
        print("Moving on...")
        break
    if ans != "y" or ans != "n":
        print("Invalid: Must be y/n")
        continue
