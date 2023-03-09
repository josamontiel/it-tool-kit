#!/usr/bin/env python

import os
import subprocess
import sys

# Function to check if a command is installed
def is_command_installed(cmd):
    return subprocess.call(f"which {cmd}", shell=True, 
stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

# Check if necessary commands are installed
if not is_command_installed("ping"):
    print("Error: ping command not found")
    sys.exit(1)
if not is_command_installed("netstat"):
    print("Error: netstat command not found")
    sys.exit(1)

# Function to ping a host and return True if successful, False otherwise
def ping(host):
    return subprocess.call(f"ping -c 1 {host}", shell=True, 
stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

# Function to check if a port is open on a host
def is_port_open(host, port):
    return subprocess.call(f"netstat -an | grep -E ^{host}\.\d+.*LISTEN.*{port}/'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

# Main function
def main():
    if len(sys.argv) < 3:
        print("Usage: it_script.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = sys.argv[2]

    # Ping the host
    if not ping(host):
        print(f"Error: {host} is not responding to pings")
        sys.exit(1)

    # Check if the port is open
    if not is_port_open(host, port):
        print(f"Error: {port} is not open on {host}")
        sys.exit(1)

    # If we got here, everything is OK
    print(f"{host}:{port} is reachable")

if __name__ == "__main__":
    main()
'''
This script checks if the ping and netstat commands are 
installed, and then pings a specified host and checks if a 
specified port is open on that host. If both tests pass, it 
prints a success message. If either test fails, it prints an 
error message and exits with a non-zero exit code.

To use the script, save it to a file (e.g. it_script.py) and 
make it executable (chmod +x it_script.py). Then run it with two 
arguments: the host and port to test (e.g. ./it_script.py 
google.com 80).
 '''
