import hashlib # Allows for hashing of passwords for storage
import getpass # getpass allows for no chars to be shown as p/w is being typed


password_manager = {}

def create_account():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")
    
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest() 
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password!")
        
def main():
    while True:
        choice = int(input("""
Enter 1 to create an account
                           
Enter 2 to login
                           
Enter 3 to exit
                           
Select: """))
        if choice == 1:
            create_account()
        elif choice == 2:
            login()
        elif choice == 3:
            break
        else:
            print("Invalid Selection!")
            
if __name__ == "__main__":
    main()