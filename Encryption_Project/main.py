from cryptography.fernet import Fernet
import os

# Function to generate a key and save it to a file
def generate_and_save_key(filename='secret.key'):
    key = Fernet.generate_key()
    with open(filename, 'wb') as key_file:
        key_file.write(key)
    print(f"Key generated and saved to {filename}")
    return key

# Function to load a key from a file
def load_key(filename='secret.key'):
    if os.path.exists(filename):
        with open(filename, 'rb') as key_file:  # Open in binary mode since fernet class is required to read key as bytes
            key = key_file.read()
        print(f"Key loaded from {filename}")
        return key
    else:
        print(f"Key file {filename} not found. Please generate a key first.")
        return None

# Function to encrypt a message
def encrypt_message(key, message):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(key, encrypted_message):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

# Function to display a menu and handle user input
def main():
    key = load_key()  # Try to load the key initially
    while True:
        print("\nMenu:")
        print("1. Generate and save key")
        print("2. Encrypt a message")
        print("3. Decrypt a message")
        print("4. Exit")
        choice = input("Enter your choice: ")

#should use switch case lol
        if choice == '1':
            key = generate_and_save_key()

        elif choice == '2':
            if key:
                message = input("Enter the message to encrypt: ")
                encrypted_message = encrypt_message(key, message)
                print(f"Encrypted message: {encrypted_message.decode()}")

            else:
                print("Please generate or load a key first.")

        elif choice == '3':
            if key:
                encrypted_message = input("Enter the encrypted message: ").encode()
                try:
                    decrypted_message = decrypt_message(key, encrypted_message)
                    print(f"Decrypted message: {decrypted_message}")
                except Exception as e:
                    print(f"Failed to decrypt message: {e}")
            else:
                print("Please generate or load a key first.")
                
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

