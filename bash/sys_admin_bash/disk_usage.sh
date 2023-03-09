#!/bin/bash

# Set the threshold for disk usage (in bytes)
THRESHOLD=5000000000

# Get the current disk usage
DISK_USAGE=`df -P / | tail -n 1 | awk '{print $4}'`

# Check if the disk usage exceeds the threshold
if [ $DISK_USAGE -gt $THRESHOLD ]; then
  # Send an alert email to the sys admin
  echo "Disk usage is at $DISK_USAGE bytes, exceeding the threshold of $THRESHOLD bytes" | mail -s "Disk usage alert" admin@example.com
fi
