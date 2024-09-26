#!/bin/bash

# Define the process name
read -p 'Please enter the name of the process to be checked : ' PROCESS

# Define the log file
LOGFILE="/home/yogeesh/bash_assignment/process_check.log"

# Check if the process is running
if pgrep -x "$PROCESS" > /dev/null
then
    echo "$(date): $PROCESS is running." >> "$LOGFILE"
else
    echo "$(date): $PROCESS is not running. Starting $PROCESS..." >> "$LOGFILE"
    systemctl start $PROCESS
    
    # Check if the start was successful
    if pgrep -x "$PROCESS" > /dev/null
    then
        echo "$(date): Successfully started $PROCESS." >> "$LOGFILE"
    else
        echo "$(date): Failed to start $PROCESS." >> "$LOGFILE"
    fi
fi

