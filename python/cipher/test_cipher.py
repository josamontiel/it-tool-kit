import unittest
from cipher import encrypt, decrypt

encrypt()

class CipherTestCase(unittest.TestCase):
    def encrypt(message, key: int):
    
        shift = key % 26
        cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    
        encrypted_message = message.lower().translate(cipher)
    
        return encrypted_message
    
if __name__ == '__main__':
    unittest.main()