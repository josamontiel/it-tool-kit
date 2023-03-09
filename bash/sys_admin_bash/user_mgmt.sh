#!/bin/bash

# Add a new user
add_user() {
  echo "Enter the username: "
  read username
  adduser $username
}

# Delete an existing user
delete_user() {
  echo "Enter the username: "
  read username
  userdel -r $username
}

# Change a user's password
change_password() {
  echo "Enter the username: "
  read username
  passwd $username
}

# Add a user to a group
add_to_group() {
  echo "Enter the username: "
  read username
  echo "Enter the group name: "
  read groupname
  usermod -aG $groupname $username
}

# Display menu options
echo "Select an option:"
echo "1. Add a user"
echo "2. Delete a user"
echo "3. Change a user's password"
echo "4. Add a user to a group"

# Read the user's choice
read choice

# Call the appropriate function based on the user's choice
case $choice in
  1)
    add_user
    ;;
  2)
    delete_user
    ;;
  3)
    change_password
    ;;
  4)
    add_to_group
    ;;
  *)
    echo "Invalid option"
    ;;
esac
