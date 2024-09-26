#!/bin/bash

# Define the threshold
THRESHOLD=80

# Email details
TO="yogeshatigre2000@gmail.com"  # Replace with the administrator's email address
SUBJECT="Disk Usage Alert for Root Filesystem"
MESSAGE="Warning: The root filesystem usage is at"

while true; do
    # Get the current disk usage of the root filesystem
    USAGE=$(df -kh / | grep / | awk '{print $5}' | sed 's/%//')

    # Check if disk usage is above the threshold
    if [ "$USAGE" -gt "$THRESHOLD" ]; then
        echo "$MESSAGE ${USAGE}%" | mail -s "$SUBJECT" "$TO"
        echo "Alert sent to $TO: Root filesystem usage is at ${USAGE}%."
    else
        echo "Disk usage is below threshold: ${USAGE}%." | mail -s "$SUBJECT" "$TO"
    fi

    # Wait for 10 minutes before checking again
    sleep 5  # 600 seconds = 10 minutes
done

