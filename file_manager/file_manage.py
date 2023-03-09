#!/bin/env python3

import argparse
import os
import csv
import sqlite3
from cryptography.fernet import Fernet

# Define the command-line arguments
parser = argparse.ArgumentParser(description='File manager')
parser.add_argument('directory', metavar='DIR', type=str,
                    help='the directory to manage')
parser.add_argument('--encrypt', action='store_true',
                    help='encrypt the file list')
parser.add_argument('--decrypt', action='store_true',
                    help='decrypt the file list')
parser.add_argument('--query', metavar='QUERY', type=str,
                    help='query the file list with SQLite')

# Define the encryption key
key = b'your-key-here'

# Define the CSV header and file name
header = ['name', 'path', 'size']
csv_file = 'file_list.csv'

# Define the SQLite table and database name
table = 'files'
database = 'file_manager.db'

def encrypt_file(file_name):
    """Encrypts a file using the key"""
    with open(file_name, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_name, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(file_name):
    """Decrypts a file using the key"""
    with open(file_name, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)
    with open(file_name, 'wb') as f:
        f.write(decrypted_data)

def write_csv(directory):
    """Writes the file list to a CSV file"""
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                file_size = os.path.getsize(file_path)
                writer.writerow([filename, file_path, 
file_size])
    if args.encrypt:
        encrypt_file(csv_file)

def read_csv():
    """Reads the file list from a CSV file"""
    if args.decrypt:
        decrypt_file(csv_file)
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        file_list = [row for row in reader]
    return file_list

def create_database():
    """Creates the SQLite database and table"""
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f'CREATE TABLE {table} (name text, path text, size 
integer)')
    conn.commit()
    conn.close()

def insert_data(file_list):
    """Inserts the file list into the SQLite database"""
    conn = sqlite3.connect(database)
    c = conn.cursor()
    for file_data in file_list:
        c.execute(f'INSERT INTO {table} VALUES (?, ?, ?)', 
file_data)
    conn.commit()
    conn.close()

def query_database(query):
    """Queries the SQLite database"""
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(query)
    results = c.fetchall()
    for row in results:
        print(row)
    conn.close()

if __name__ == '__main__':
    # Parse the command-line arguments
    args = parser.parse_args()

    # Write the file list to a CSV file

    write_csv(args.directory)

    # Read the file list from the CSV file
    file_list = read_csv()

    # Create the database and insert the data
    create_database()
    insert_data(file_list)

    # Query the database if a query is provided
    if args.query:
        query_database(args.query)

