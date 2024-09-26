#!/bin/bash

# Check if a file argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Check if the file exists
if [ ! -e "$1" ]; then
    echo "File '$1' does not exist."
    exit 1
fi

# Initialize variables for permissions
read_permission="no"
write_permission="no"
execute_permission="no"

# Check for read permission
if [ -r "$1" ]; then
    read_permission="yes"
fi

# Check for write permission
if [ -w "$1" ]; then
    write_permission="yes"
fi

# Check for execute permission
if [ -x "$1" ]; then
    execute_permission="yes"
fi

# Display results based on combinations
echo "File '$1' permissions:"
if [ "$read_permission" = "yes" ] && [ "$write_permission" = "yes" ] && [ "$execute_permission" = "yes" ]; then
    echo "The file has read, write, and execute permissions."
elif [ "$read_permission" = "yes" ] && [ "$write_permission" = "yes" ] && [ "$execute_permission" = "no" ]; then
    echo "The file has read and write permissions, but not execute permission."
elif [ "$read_permission" = "yes" ] && [ "$write_permission" = "no" ] && [ "$execute_permission" = "yes" ]; then
    echo "The file has read and execute permissions, but not write permission."
elif [ "$read_permission" = "yes" ] && [ "$write_permission" = "no" ] && [ "$execute_permission" = "no" ]; then
    echo "The file has read permission only."
elif [ "$read_permission" = "no" ] && [ "$write_permission" = "yes" ] && [ "$execute_permission" = "yes" ]; then
    echo "The file has write and execute permissions, but not read permission."
elif [ "$read_permission" = "no" ] && [ "$write_permission" = "yes" ] && [ "$execute_permission" = "no" ]; then
    echo "The file has write permission only."
elif [ "$read_permission" = "no" ] && [ "$write_permission" = "no" ] && [ "$execute_permission" = "yes" ]; then
    echo "The file has execute permission only."
else
    echo "The file has no read, write, or execute permissions."
fi

