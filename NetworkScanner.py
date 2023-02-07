import scapy.all as scapy # importing scapy module
import re # importing regular expression module
import time # importing time module

print("""
 __  __      ____  _            _    _           _   
|  \/  |_ __| __ )| | __ _  ___| | _| |__   __ _| |_ 
| |\/| | '__|  _ \| |/ _` |/ __| |/ / '_ \ / _` | __|
| |  | | | _| |_) | | (_| | (__|   <| | | | (_| | |_ 
|_|  |_|_|(_)____/|_|\__,_|\___|_|\_\_| |_|\__,_|\__|
""")

ipregex=re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$") # regular expression to match IP address range

print("__"*30)
print("[*]Welcome Buddy....")
time.sleep(1)
print("\n[*]How to Use This Tool...")
time.sleep(1)
print("""
For Example
Enter IP Address Range: 192.168.0.0/24            
""")
print("__"*30)

try:
    IP=input("\n[*]Enter IP Address Range: ") # user input for IP address range
except KeyboardInterrupt:
    time.sleep(0.75)
    print("\n\n[*]Quitting...............")
    exit()

while True:
    if ipregex.search(IP): # check if input matches the regular expression for IP address range
        print(f"{IP} is a Valid IP address range")
        break
Result=scapy.arping(IP) # use scapy's arping function to ping the IP address range
