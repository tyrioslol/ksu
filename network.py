import os
import sys

if not os.geteuid()==0:
    sys.exit('This script must be run as root!')

# update if you want 
while True:
    print("\nWould you like to update now? (y/n)")
    ans = input()
    if ans == "y":
        print("Updating...")
        os.system("sudo apt-get update && sudo apt-get upgrade -y")
        break
    if ans == "n":
        print("Moving on...")
        break
    if ans != "y" or ans != "n":
        print("Invalid: Must be y/n")
        continue

# Install git
print("\nInstalling git...")
os.system("sudo apt-get install git | 2>/dev/null")
print("Done")
os.system("which git")

# Install wget
print("\nInstalling wget...")
os.system("sudo apt-get install wget | 2>/dev/null")
print("Done")
os.system("which wget")

# Install python3
print("\nInstalling python...")
os.system("sudo apt-get install python3 | 2>/dev/null")
print("Done")
os.system("which python3")

# Install UFW
print("\nInstalling UFW...")
os.system("sudo apt-get install ufw | 2>/dev/null")
print("Done")
os.system("which ufw")

# Installing nmap
print("\nInstalling nmap...")
os.system("sudo apt-get install nmap | 2>/dev/null")
print("Done")
os.system("which nmap")
print("\nScanning...")
os.system("nmap -sT -sV localhost > scan.txt")
print("Done, results saved to scan.txt.")

# Install netstat/nettools
print("\nInstalling net-tools/netstat...")
os.system("sudo apt-get install net-tools | 2>/dev/null")
print("Done")
os.system("which netstat")
os.system("sudo netstat -tulpn | grep LISTEN > netstat.txt")
print("Done, results saved to netstat.txt.")

# Importing linpeas
print("\nGetting linpeas and running local scan...")
os.system("wget https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh && chmod +x linpeas.sh")

while True:
    print("\nWould you like to run linpeas now? (y/n)")
    ans = input()
    if ans == "y":
        print("Scanning...")
        os.system("./linpeas.sh > linpeas.txt")
        print("Done")
        break
    if ans == "n":
        print("Moving on...")
        break
    if ans != "y" or ans != "n":
        print("Invalid: Must be y/n")
        continue
