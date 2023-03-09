import os
import platform
import subprocess

'''
This script first gets the operating system that it's running on 
and prints it to the console. Then, it runs a command to get the 
IP configuration information and prints the output to the 
console.

Next, it creates a new directory if it doesn't already exist. 
Finally, it gets the current user's home directory and prints it 
to the console.

This script could be useful for IT professionals who need to 
perform system administration tasks, such as checking network 
configurations, creating directories, and getting user 
information.
 '''

# Get the operating system and print it to the console
operating_system = platform.system()
print(f"The operating system is {operating_system}")

# Run a command and print the output to the console
command = "ipconfig" if operating_system == "Windows" else "ifconfig"
output = subprocess.check_output(command, 
universal_newlines=True)
print(output)

# Create a new directory if it doesn't exist
directory_path = ("C:\\Program Files\\MyApp" 
                  if operating_system == "Windows" 
                  else "/usr/local/MyApp")
if not os.path.exists(directory_path):
    os.makedirs(directory_path)
    print(f"Created directory {directory_path}")

# Get the current user's home directory
home_directory = os.path.expanduser("~")
print(f"The home directory is {home_directory}")


