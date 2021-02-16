#!/usr/bin/python3

import os

# Installing nmap
print("\nINSTALL NMAP:")
os.system("sudo apt-get install nmap && echo Done")
print("Scanning...")
os.system("nmap -sT -sV localhost | tee services.txt && echo Done")

# Install netstat/nettools
print("\nINSTALL NET-TOOLS:")
os.system("sudo apt-get install net-tools && sudo netstat -tulpn | grep LISTEN | tee netstat.txt && echo Done")