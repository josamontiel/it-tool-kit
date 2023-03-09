#!/usr/bin/env python3

"""
This script performs various system administration tasks using 
Python standard libraries.

Tasks performed:
- Get system information (hostname, OS, kernel version, CPU, 
memory, disk space)
- Check system uptime
- Get list of running processes
- Restart a service
"""

import os
import platform
import psutil
import subprocess
import sys
import time


# Function to get system information
def get_system_info():
    hostname = platform.node()
    os_name = platform.system()
    os_version = platform.release()
    cpu = platform.processor()
    memory = psutil.virtual_memory().total
    disk = psutil.disk_usage('/').total
    print(f"Hostname: {hostname}")
    print(f"OS: {os_name} {os_version}")
    print(f"CPU: {cpu}")
    print(f"Memory: {memory} bytes")
    print(f"Disk space: {disk} bytes")


# Function to check system uptime
def check_system_uptime():
    uptime = time.time() - psutil.boot_time()
    print(f"System uptime: {uptime:.2f} seconds")


# Function to get list of running processes
def get_running_processes():
    processes = psutil.process_iter()
    print("Running processes:")
    for process in processes:
        try:
            name = process.name()
            pid = process.pid
            status = process.status()
            print(f"Name: {name}, PID: {pid}, Status: {status}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, 
psutil.ZombieProcess):
            pass


# Function to restart a service
def restart_service(service_name):
    try:
        subprocess.run(['systemctl', 'restart', service_name], 
check=True)
        print(f"{service_name} restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting {service_name}: {e}")


# Main function
def main():
    # Check if running as root
    if os.geteuid() != 0:
        print("This script must be run as root.")
        sys.exit(1)

    # Get system information
    get_system_info()

    # Check system uptime
    check_system_uptime()

    # Get list of running processes
    get_running_processes()

    # Restart a service
    service_name = 'nginx'
    restart_service(service_name)


if __name__ == '__main__':
    main()


'''
The script has the following features:

    It uses standard libraries such as os, platform, psutil, 
subprocess, sys, and time.
    The script includes functions for various system 
administration tasks such as getting system information, 
checking system uptime, getting a list of running processes, and 
restarting a service.
    The main() function calls these functions to perform the 
desired tasks.
    The script includes a check to ensure that it is run as root 
(sudo) user.
    The script includes documentation in comments to explain the 
purpose of each function and the overall script.

Note: This is just an example implementation and should not be 
used in a production environment without proper testing and 
modification to fit your specific needs.

'''
