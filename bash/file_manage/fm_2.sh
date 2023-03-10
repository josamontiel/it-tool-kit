#!/bin/bash

# FIle managaer with zenity
# Zenity is a tui for bash


while true
do
    current_dir=$(pwd)
    choice=$(zenity --list --title "File Manager" --column "Action" \
        "List files" \
        "Create directory" \
        "Create file" \
        "Delete file" \
        "Delete directory" \
        "Copy file" \
        "Move file" \
        "Change directory" \
        "Exit")

    case $choice in
        "List files")
            zenity --text-info --title "List files" --filename="$current_dir"
            ;;
        "Create directory")
            dir_name=$(zenity --entry --title "Create directory" --text "Enter directory name:")
            mkdir "$dir_name"
            ;;
        "Create file")
            file_name=$(zenity --entry --title "Create file" --text "Enter file name:")
            touch "$file_name"
            ;;
        "Delete file")
            file_name=$(zenity --file-selection --title "Delete file" --filename="$current_dir")
            if [ "$file_name" != "" ]; then
                zenity --question --title "Delete file" --text "Are you sure you want to delete the file: $file_name?"
                if [ $? = 0 ]; then
                    rm -i "$file_name"
                fi
            fi
            ;;
        "Delete directory")
            dir_name=$(zenity --file-selection --title "Delete directory" --filename="$current_dir" --directory)
            if [ "$dir_name" != "" ]; then
                zenity --question --title "Delete directory" --text "Are you sure you want to delete the directory: $dir_name?"
                if [ $? = 0 ]; then
                    rm -ri "$dir_name"
                fi
            fi
            ;;
        "Copy file")
            source_file=$(zenity --file-selection --title "Copy file" --filename="$current_dir")
            if [ "$source_file" != "" ]; then
                dest_file=$(zenity --file-selection --save --title "Copy file" --filename="$current_dir")
                if [ "$dest_file" != "" ]; then
                    cp -i "$source_file" "$dest_file"
                fi
            fi
            ;;
        "Move file")
            source_file=$(zenity --file-selection --title "Move file" --filename="$current_dir")
            if [ "$source_file" != "" ]; then
                dest_file=$(zenity --file-selection --save --title "Move file" --filename="$current_dir")
                if [ "$dest_file" != "" ]; then
                    mv -i "$source_file" "$dest_file"
                fi
            fi
            ;;
        "Change directory")
            dir_name=$(zenity --file-selection --title "Change directory" --filename="$current_dir" --directory)
            if [ "$dir_name" != "" ]; then
                cd "$dir_name"
            fi
            ;;
        "Exit")
            zenity --question --title "Exit" --text "Are you sure you want to exit?"
            if [ $? = 0 ]; then
                exit 0
            fi
            ;;
        *)
            zenity --error --title "Invalid choice" --text "Invalid choice: $choice"
            ;;
    esac
done
