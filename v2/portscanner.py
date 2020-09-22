#!/bin/python3
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

# input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
print("\n")

t1 = datetime.now()

# banner
print("="*60)
print("Scanning remote host", remoteServerIP)
print("Scan started at {}".format(t1))
print("="*60)
print("\n")

# specify ports

# error handling
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Terminating...")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Terminating...")
    sys.exit()

except socket.error:
    print("Could not connect to the server")
    sys.exit()

t2 = datetime.now()
totalTime = t2 - t1

print("Scan completed in {}".format(totalTime))