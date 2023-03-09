#!/bin/bash

# set the source and destination directories
SOURCE_DIR="/path/to/source/directory"
DEST_DIR="/path/to/backup/directory"

# create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# create a timestamped directory for the backup
TIMESTAMP=$(date +%Y%m%d%H%M%S)
BACKUP_DIR="$DEST_DIR/$TIMESTAMP"
mkdir "$BACKUP_DIR"

# copy the files from the source directory to the backup 
directory
rsync -av "$SOURCE_DIR/" "$BACKUP_DIR/"

# display a message indicating the backup is complete
echo "Backup complete: $BACKUP_DIR"

