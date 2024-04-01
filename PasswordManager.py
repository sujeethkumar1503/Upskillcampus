import getpass
import hashlib
import secrets

def generate_salt():
    return secrets.token_hex(16)

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

def save_password(username, password):
    with open("passwords.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    print("Password saved successfully.")

def retrieve_password(username):
    with open("passwords.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if stored_username == username:
                return stored_password
    return None

def generate_password(length=12):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-"
    return "".join(secrets.choice(alphabet) for _ in range(length))

def main():
    print("Welcome to the Password Manager!")
    while True:
        print("\nMenu:")
        print("1. Save password")
        print("2. Retrieve password")
        print("3. Generate random password")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            salt = generate_salt()
            hashed_password = hash_password(password, salt)
            save_password(username, f"{hashed_password}:{salt}")
        elif choice == "2":
            username = input("Enter username: ")
            password = getpass.getpass("Enter master password: ")
            stored_password = retrieve_password(username)
            if stored_password:
                hashed_password, salt = stored_password.split(":")
                if hash_password(password, salt) == hashed_password:
                    print(f"Password for {username}: {hashed_password}")
                else:
                    print("Incorrect master password.")
            else:
                print("Password not found.")
        elif choice == "3":
            length = int(input("Enter password length (default 12): "))
            print("Generated password:", generate_password(length))
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if _name_ == "_main_":
    main()