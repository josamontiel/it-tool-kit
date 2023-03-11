#!/usr/bin/env python3

"""
Python Port Scanner using Standard Libraries

This script scans all TCP ports on a target host and prints a message indicating which ports are open.

Usage: python3 port_scanner.py <target_host>

Example: python3 port_scanner.py 192.168.1.1
"""

import argparse
import socket
import threading

def scan_port(target_host, port):
    # Attempt to connect to a single port on the target host
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout of 0.5 seconds to avoid blocking for too long
        sock.settimeout(0.5)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            # If the connection was successful, print a message indicating that the port is open
            print("Port {}: Open".format(port))
        sock.close()
    except socket.error:
        # If there was an error connecting to the port, ignore it and move on to the next port
        pass

def scan_target(target_host):
    # Scan all ports on the target host
    print("Scanning ports on {}...\n".format(target_host))
    threads = []
    for port in range(1, 1025):
        # Start a new thread to scan each port concurrently
        thread = threading.Thread(target=scan_port, args=(target_host, port))
        threads.append(thread)
        thread.start()
    # Wait for all threads to finish before returning
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Parse command-line arguments using argparse
    parser = argparse.ArgumentParser(description="Python port scanner using standard libraries")
    parser.add_argument("target_host", type=str, help="IP address of target host")
    args = parser.parse_args()
    # Call the main function to scan the target host
    scan_target(args.target_host)
