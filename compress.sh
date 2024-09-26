#!/bin/bash

# Set the directories
source_dir="/home/user/documents"
backup_dir="/home/user/backup"
backup_file="documents_backup"

# Check if the backup directory exists, if not create it
if [ ! -d "$backup_dir" ]; then
    mkdir -p "$backup_dir"
fi

# Create the tarball and move it to the backup directory
tar -czf "$backup_dir/$backup_file.tar.gz" -C "$source_dir" .

# Notify completion
echo "Backup of $source_dir completed and moved to $backup_dir/$backup_file"

