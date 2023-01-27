import scapy.all as scapy
import re
import time
import pyfiglet
text=pyfiglet.figlet_format("Mr.Blackhat")
print(text)

ipregex=re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

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
    IP=input("\n[*]Enter IP Address Range: ") 
except KeyboardInterrupt:
    time.sleep(0.75)
    print("\n\n[*]Quitting...............")
    exit()

while True:
    if ipregex.search(IP):
        print(f"{IP} is a Valid IP address range")
        break
Result=scapy.arping(IP)