#!/bin/bash

# Prompt the user for the file to encrypt
echo "Enter the path to the file you want to encrypt:"
read FILE

# Prompt the user for the recipient's public key
echo "Enter the recipient's public key ID:"
read RECIPIENT_KEY_ID

# Encrypt the file using GPG
gpg --recipient $RECIPIENT_KEY_ID --output $FILE.gpg --encrypt $FILE

# Display a message indicating that the file has been encrypted
echo "File encrypted successfully. The encrypted file is located at $FILE.gpg"

: '

This script prompts the user to enter the path to the file they want to encrypt and the ID of the recipients public key. It then uses GPG to encrypt the file and save the encrypted version with a ".gpg" file extension. Finally, it displays a message indicating that the file has been encrypted and provides the path to the encrypted file.

Note that the recipients public key must be imported into your GPG keyring before you can use it to encrypt a file. You can import a public key using the following command:

vbnet

gpg --import /path/to/public/key/file.asc

Replace "/path/to/public/key/file.asc" with the actual path to the public key file.

'