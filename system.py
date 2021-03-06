import os
import sys
import subprocess

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

# backup services
svc_config_backup = input("\n>>> Create backups of config files? Type y or n, then hit enter:  ")
if svc_config_backup == "y":
    svc_name = input("\n>>> What is the scored service? Type openvpn, wordpress, mysql, or docker:  ")
    if svc_name == "openvpn":
        os.system("cp -r /etc/openvpn /home/openvpn")
        print("\n>>> backups saved to /home/openvpn")
    elif svc_name == "wordpress":
        os.system("cp -r /etc/apache2/apache2.conf /home/apache")
        print("\n>>> backups saved to /home/apache")
    elif svc_name == "mysql":
        os.system("cp -r /etc/my.cnf /home/mysql")
        print("\n>>> backups saved to /home/mysql")
    elif svc_name == "docker":
        os.system("cp -r /etc/docker /home/docker-frometc")
        os.system("cp -r /var/lib/docker /home/docker-fromvar")
        print("\n>>> backups saved to /home/docker")
    else:
        print("\n>>> Unknown service.")
else:
    print("\n>>> OK")

# Getting user info from /etc/passwd
users = os.system("cat /etc/passwd > users.txt")

# Make list from output
userslist = ''

with open("users.txt", "r") as f:
    for line in f:
        userslist += line


# Getting shell info from /etc/shells
shells = os.system("cat /etc/shells > .shells")

# Make list from output
shelllist = ''
with open(".shells", "r") as f:
    for line in f:
        shelllist += line

# Print users with shells
print("USERS WITH SHELLS:")
for line in userslist.splitlines():
    for ln in shelllist.splitlines():
        if "nologin" in line:
            continue
        if ln in line:
            print(line)
print("Full users in users.txt...\n")

while True:
    print("\nWould you like to remove any users? (y/n)")
    ans = input()
    if ans == "y":
        user = input("Which user would you like to remove?")
        os.system("deluser " + user + " && rm -rf /home/" + user)
    if ans == "n":
        print("Moving on...")
        break
    if ans != "y" and ans != "n":
        print("Invalid: Must be y/n")
        continue

os.system("clear")
input("Done: Press Enter to continue...")
os.system("clear")

###GROUPS###
# Get group info from /etc/group
groups = os.system("cat /etc/group > groups.txt")

# Making group list from output
grouplist = ''

with open("groups.txt", "r") as f:
    for line in f:
        grouplist += line

###SUDOERS###
# Get sudoers info from /etc/sudoers and print findings
results = subprocess.check_output(["cat", "/etc/sudoers"])

print("SUDO PERMISSIONS:")
sudoerslist = results.decode().splitlines()
for line in sudoerslist:
    if line.startswith("Defaults"):
        continue
    if line.startswith("#"):
        continue
    if "%" in line:
        print("Group: ", line)
        continue
    if "=" in line:
        print("User: ", line)

while True:
    print("\nWould you like to remove any sudoers (This must be done manually from the sudoers file)? (y/n)")
    ans = input()
    if ans == "y":
        os.system("visudo")
    if ans == "n":
        print("Moving on...")
        break
    if ans != "y" and ans != "n":
        print("Invalid: Must be y/n")
        continue

os.system("clear")
input("Done: Press Enter to continue...")
os.system("clear")

print("Looking for sudo group members...")
os.system("cat /etc/group | grep sudo")

while True:
    print("\nWould you like to remove a user from the sudo group? (y/n)")
    ans = input()
    if ans == "y":
        user = input("What user would you like to remove from the sudo group?")
        os.system("deluser " + user + " sudo")
    if ans == "n":
        print("Moving on...")
        break
    if ans != "y" and ans != "n":
        print("Invalid: Must be y/n")
        continue

os.system("clear")

print("Looking for admin group members...")
os.system("cat /etc/group | grep admin")

while True:
    print("\nWould you like to remove a user from the admin group? (y/n)")
    ans = input()
    if ans == "y":
        user = input("What user would you like to remove from the admin group?")
        os.system("deluser " + user + " admin")
    if ans == "n":
        print("Moving on...")
        break
    if ans != "y" and ans != "n":
        print("Invalid: Must be y/n")
        continue

os.system("cat /etc/group > groups.txt")
print("Full groups saved to groups.txt...")
input("Done: Press Enter to continue...")
os.system("clear")

# Show files with sensitive permissions
print("SENSITIVE PERMISSIONS: (Should be -rw-r--r-- and -rw-r-----)")
os.system("ls -al /etc/passwd && ls -al /etc/shadow")
os.system("find / -user root -type f -perm 777 2>/dev/null")
os.system("find / -user root -type f -perm 766 2>/dev/null")

print("\nFinding Files with SUID...")
os.system("find / -perm /4000 -user root -type f 2>/dev/null > .suid")
print("Done, file saved to .suid.")
print("\nFinding Files with GUID...")
os.system("find / -perm /2000 -type f 2>/dev/null > .guid")
print("Done, file saved to .guid.")

print("\nAll done, thanks for playing!")
