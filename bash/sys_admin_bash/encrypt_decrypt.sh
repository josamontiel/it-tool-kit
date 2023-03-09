#!/bin/bash

# Prompt the user to choose an operation
echo "Choose an operation:"
echo "1. Encrypt a file"
echo "2. Decrypt a file"
read OPERATION

if [ $OPERATION -eq 1 ]; then
  # Encrypt a file

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

elif [ $OPERATION -eq 2 ]; then
  # Decrypt a file

  # Prompt the user for the file to decrypt
  echo "Enter the path to the file you want to decrypt:"
  read ENCRYPTED_FILE

  # Decrypt the file using GPG
  gpg --output ${ENCRYPTED_FILE%.*} --decrypt $ENCRYPTED_FILE

  # Display a message indicating that the file has been decrypted
  echo "File decrypted successfully. The decrypted file is located at ${ENCRYPTED_FILE%.*}"

else
  # Invalid operation

  echo "Invalid operation. Please choose 1 or 2."
fi

: '

This script prompts the user to choose between encrypting and decrypting a file. If the user chooses to encrypt a file, the script prompts them for the file to encrypt and the ID of the recipients public key. It then uses GPG to encrypt the file and saves the encrypted version with a ".gpg" file extension. If the user chooses to decrypt a file, the script prompts them for the encrypted file and decrypts it using GPG, saving the decrypted version without the ".gpg" extension. Finally, the script displays a message indicating that the file has been encrypted or decrypted and provides the path to the encrypted or decrypted file.

Note that in the decryption section of the script, ${ENCRYPTED_FILE%.*} is used to remove the ".gpg" extension from the file name when saving the decrypted version. This is achieved using parameter expansion, which removes the shortest match of ".*" (i.e., any characters after a dot) from the end of the variable value.

'