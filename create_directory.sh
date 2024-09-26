#!/bin/bash

#To store the argunments passed on the command line
NUMBER_OF_PARAMETERS="${#}"

#To set a default path for directory creation
DEFAULT_PATH="/home/user/"

#To check if the user has passed any arguments or not
if [[ "${NUMBER_OF_PARAMETERS}" -lt 1 ]]
then
	echo "No path given , Hence setting default path ${DEFAULT_PATH} "
fi

#List of directories to be created 
DIRS=("projects/project1" "projects/project2" "projects/project3" "documents" "downloads")


#Using a loop to iterates over each entry of above mentioned list of directories
#Expands the list/array into individual directory paths (${DIRS[@]})
for dir in "${DIRS[@]}"; 
do
    mkdir -p "$DEFAULT_PATH/$dir"
done

#Success Message
echo "Directories created successfully"

#List contents of directories in a tree-like format
tree ${DEFAULT_PATH}
