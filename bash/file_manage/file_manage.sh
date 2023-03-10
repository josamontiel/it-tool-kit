#!/bin/bash

while true
do
    echo "Current directory: $(pwd)"
    echo "------------------------"
    echo "Select an action:"
    echo "1) List files"
    echo "2) Create directory"
    echo "3) Create file"
    echo "4) Delete file"
    echo "5) Delete directory"
    echo "6) Copy file"
    echo "7) Move file"
    echo "8) Change directory"
    echo "9) Exit"
    read choice

    case $choice in
        1)
            ls -al
            ;;
        2)
            echo "Enter directory name:"
            read dir_name
            mkdir $dir_name
            ;;
        3)
            echo "Enter file name:"
            read file_name
            touch $file_name
            ;;
        4)
            echo "Enter file name to delete:"
            read file_name
            rm -i $file_name
            ;;
        5)
            echo "Enter directory name to delete:"
            read dir_name
            rm -ri $dir_name
            ;;
        6)
            echo "Enter source file name:"
            read source_file
            echo "Enter destination file name:"
            read dest_file
            cp $source_file $dest_file
            ;;
        7)
            echo "Enter source file name:"
            read source_file
            echo "Enter destination file name:"
            read dest_file
            mv $source_file $dest_file
            ;;
        8)
            echo "Enter directory name:"
            read dir_name
            cd $dir_name
            ;;
        9)
            echo "Exiting file manager."
            exit 0
            ;;
        *)
            echo "Invalid choice."
            ;;
    esac
done
