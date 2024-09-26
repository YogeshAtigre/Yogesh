#!/bin/bash


# Check if the directory argument is provided
if [[ -z "$1" ]]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# To take source as input from user
SRC_DIR=$1

# To Check if the source directory already exists
if [[ ! -d "$SRC_DIR" ]]
then
	echo "$SRC_DIR , does not exists please check"
	exit 1
fi

# Create a timestamp for the backup directory
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# To create backup directory
BKP_DIR="$SOURCE_DIR/backup_$TIMESTAMP"

mkdir -p "$BKP_DIR"

# To copy all the .txt files to backup directory
cp "$SRC_DIR" /.*txt "$BKP_DIR"

# Check if the copy operation was successful
if [ $? -eq 0 ]; then
    echo "Backup created at $BACKUP_DIR"
else
    echo "No .txt files found or failed to copy."
fi
