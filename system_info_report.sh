#!/bin/bash

#Taking the script interval run time from the user as an optional argunment

read -p 'Please enter the interval (in sec) at which the report is to be generated ' INTERVEL

#Report file name
FILE_NAME=system_report.txt

#Memory info of the system 
Memroy=$(free -h)

#Disk space info of the system 
Disk_space=$(df -kh)

#Up time of the system
system_uptime=$(uptime -p)

# CPU load of the system 
cpu_load=$(top -bn1 | grep "load average" | awk '{print $12 $13 $14}')

# to check top 10 current running processes and sort them acoording to memory usage 
processes=$(ps -eo pid,comm,%mem,%cpu --sort=-%mem | head -n 10)

while true;do
	# Create the report
	echo "=== System Information Report ===" > $FILE_NAME
	echo "Generated on: $(date)" >> $FILE_NAME
	echo "" >> $FILE_NAME

	echo "1. System Uptime:" >> $FILE_NAME
	echo "$uptime_info" >> $FILE_NAME
	echo "" >> $FILE_NAME

	echo "2. Memory Usage:" >> $FILE_NAME
	echo "$memory_info" >> $FILE_NAME
	echo "" >> $FILE_NAME

	echo "3. CPU Load (last 1, 5, 15 minutes):" >> $FILE_NAME
	echo "$cpu_load" >> $FILE_NAME
	echo "" >> $FILE_NAME

	echo "4. Disk Usage:" >> $FILE_NAME
	echo "$disk_usage" >> $FILE_NAME
	echo "" >> $FILE_NAME

	echo "5. Top 10 Running Processes (by memory usage):" >> $FILE_NAME
	echo "$processes" >> $FILE_NAME

	# Notify the user
	echo "System information report saved to $FILE_NAME"

	
	sleep $INTERVEL
	echo "Sleeping for $INTERVEL sec" >> $FILE_NAME
	echo "==================================================" >> $FILE_NAME
done
