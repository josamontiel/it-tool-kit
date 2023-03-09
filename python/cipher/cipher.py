########################################
# Caesar cipher project                #
# NOT TO BE USED FOR SECURE MESSAGING  #
########################################

import string

def encrypt(message, key: int):
    
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    
    encrypted_message = message.lower().translate(cipher)
    
    return encrypted_message

def decrypt(encrypted_message, key: int):
    
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    message = encrypted_message.translate(cipher)
    return message

message = input('\nPlease type the message you wish to encrypt: ')

key = int(input('\nHow many places would you like letters shifted by: '))

encrypted_message = encrypt(message, key)
print(f'\nHere is your encrypted message:\n{encrypted_message}\n')

decrypted_message = decrypt(encrypted_message, key)
print(f'\nHere is your decrypted message:\n{decrypted_message}\n')
