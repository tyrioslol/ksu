import os
import sys
import subprocess

if not os.geteuid()==0:
    sys.exit('This script must be run as root!')

# uncomment this line for update & root password
# os.system("passwd")
# os.system("sudo apt-get update && sudo apt-get upgrade -y")


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
results = subprocess.run(["cat", "/etc/sudoers"], stdout=subprocess.PIPE)

print("SUDO PERMISSIONS:")
sudoerslist = results.stdout.decode().splitlines()
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

os.system("cat /etc/group > groups.txt")
print("Full groups saved to groups.txt...")

# Show files with sensitive permissions
print("\nSENSITIVE PERMISSIONS: (Should be -rw-r--r-- and -rw-r-----)")
os.system("ls -al /etc/passwd && ls -al /etc/shadow")
os.system("find / -user root -type f -perm 777 2>/dev/null")
os.system("find / -user root -type f -perm 766 2>/dev/null")

print("\nFinding Files with SUID...")
os.system("find / -perm /4000 -user root -type f 2>/dev/null > .suid")
print("Done, file saved to .suid.")
print("\nFinding Files with GUID...")
os.system("find / -perm /2000 -type f 2>/dev/null > .guid")
print("Done, file saved to .guid.")
