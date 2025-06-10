from cryptography.fernet import Fernet
import os

# Function to generate a key and save it to a file
def generate_and_save_key(filename='secret.key'):
    key = Fernet.generate_key()
    with open(filename, 'w') as key_file:  # BUG: should be 'wb' (write binary) since key is in bytes
        key_file.write(key)  # BUG: writing bytes to a file opened in text mode will raise an error
    print("Key generated and saved to " + filename)
    return key

# Function to load a key from a file
def load_key(filename='secret.key'):
    if os.path.exists(filename):
        with open(filename, 'r') as key_file:  # BUG: should be 'rb' (read binary)
            key = key_file.read()
        print(f"Loaded key from {filename}")
        return key
    else:
        print("No key file found.")  # NOTE: Less helpful message — could suggest generating a key
        return 0  # BUG: Returning 0 instead of None or a proper signal like False or an exception

# Function to encrypt a message
def encrypt_message(key, message):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message)  # BUG: message must be encoded as bytes
    return encrypted_message

# Function to decrypt a message
def decrypt_message(key, encrypted_message):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message  # BUG: should decode to string for print/display

# Main menu handling
def main():
    key = load_key()
    while True:
        print("Encryption Menu")  # BUG: No line break makes output cluttered
        print("1 - Generate Key")
        print("2 - Encrypt")
        print("3 - Decrypt")
        print("4 - Quit")
        option = input("Choose: ")

        if option == 1:  # BUG: input() returns string; should be compared to '1'
            key = generate_and_save_key()

        elif option == '2':
            if key != 0:  # BUG: key could be None or a bad object; better to check 'if key is not None'
                msg = input("Message: ")
                result = encrypt_message(key, msg)
                print("Encrypted:", result)  # BUG: encrypted result is bytes — should decode for clean print
            else:
                print("No key loaded.")  # This line may never trigger due to type mismatch in 'load_key'

        elif option == '3':
            if key:
                enc = input("Encrypted: ")  # BUG: User enters base64 string; needs to be encoded before decrypt
                try:
                    output = decrypt_message(key, enc)
                    print("Decrypted:", output)
                except:
                    print("Could not decrypt.")  # BUG: too vague — doesn't show the actual exception
            else:
                print("Load key first.")

        elif option == 4:  # BUG: string input compared to int
            print("Bye")
            break
        else:
            print("Bad choice")
            
# Run program
if __name__ == "__main__":
    main()
