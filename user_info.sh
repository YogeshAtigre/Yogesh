#!/bin/bash

#To store the username of the user
user_name=$(whoami)
#To store the group id of the user
GID=$(id -g)
echo "*************************************************"
echo "USER NAME : $user_name"
echo "USER ID : ${UID}"
echo "GROUP ID : ${GID}"
echo "HOME DIRECTORY : $HOME"
echo "SHELL USED : $SHELL"
echo "*************************************************"
