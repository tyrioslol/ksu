#!/usr/bin/python3
import os
import sys

if not os.geteuid()==0:
    sys.exit('This script must be run as root!')


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
# Get sudoers info from /etc/sudoers
sudoers = os.system("cat /etc/sudoers > .sudoers")

# Making sudoers list from output
sudoerslist = ''

with open(".sudoers", "r") as f:
    for line in f:
        if "ALL" in line:
            sudoerslist += line
            #.split('A')[:1]

for line in sudoerslist.splitlines():
    newline = str(line.split('A')[:1])
    #print(newline)

# Print various sensitive groups
print("\nSENSITIVE GROUPS:")
for line in grouplist.splitlines():
    for i in sudoerslist.splitlines():
        newline = str(i.split('A')[:1]).strip("[]'")
        #print(newline)
        if str(i.split('A')[:1]).strip("[]'") in line:
            print(line)
        #print(line)
print("Full groups in groups.txt...\n")


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