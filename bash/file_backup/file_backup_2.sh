#!/bin/bash

# Set source and destination directories
SRC_DIR="/home/user/Documents"
DEST_DIR="/media/user/ExternalDrive/Backup"

# Create backup directory if it doesn't exist
if [ ! -d "$DEST_DIR" ]; then
  mkdir -p "$DEST_DIR"
fi

# Backup files using rsync
rsync -avh "$SRC_DIR" "$DEST_DIR"

# Check if the backup was successful
if [ $? -eq 0 ]; then
  echo "Backup successful"
else
  echo "Backup failed"
fi

