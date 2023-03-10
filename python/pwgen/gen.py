#!/usr/bin/env python3

# MIT License

# Copyright (c) 2023 Joseph A. M. 

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import argparse
import secrets
import string

def generate_pin(length):
    """Generates a random PIN of specified length"""
    return ''.join(secrets.choice(string.digits) for i in range(length))

def generate_password(length):
    """Generates a random password of specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))

def generate_passphrase(num_words):
    """Generates a random passphrase consisting of specified number of words"""
    with open('/usr/share/dict/words') as f:
        words = [word.strip() for word in f.readlines()]
    passphrase = ' '.join(secrets.choice(words) for i in range(num_words))
    return passphrase

def main():
    parser = argparse.ArgumentParser(description='Generates passcodes')
    parser.add_argument('type', choices=['pin', 'password', 'passphrase'], help='type of passcode to generate')
    parser.add_argument('-l', '--length', type=int, default=8, help='length of passcode (for PIN and password only)')
    parser.add_argument('-w', '--num-words', type=int, default=4, help='number of words in passphrase (for passphrase only)')
    args = parser.parse_args()

    if args.type == 'pin':
        print(generate_pin(args.length))
    elif args.type == 'password':
        print(generate_password(args.length))
    elif args.type == 'passphrase':
        print(generate_passphrase(args.num_words))

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
