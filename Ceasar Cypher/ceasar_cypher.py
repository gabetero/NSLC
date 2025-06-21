# Function to encrypt a message using the Caesar Cipher
def encrypt(plain_text, key):
    cipher_text = ""

    # Loop through each character in the input text
    for char in plain_text:
        if char.isalpha():  # Only shift letters (ignore spaces, punctuation, etc.)
            ascii_offset = ord('A') if char.isupper() else ord('a')  # Adjust for upper/lowercase
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)  # Shift and wrap around alphabet
            cipher_text += encrypted_char  # Add the encrypted character to the result
        else:
            cipher_text += char  # Leave non-alphabet characters unchanged

    return cipher_text  # Return the full encrypted message


# Function to decrypt a Caesar Cipher message using the given key
def decrypt(cipher_text, key):
    plain_text = ""

    # Loop through each character in the encrypted text
    for char in cipher_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')  # Adjust for case
            decrypted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)  # Shift backwards
            plain_text += decrypted_char  # Add decrypted character to result
        else:
            plain_text += char  # Leave non-alphabet characters unchanged

    return plain_text  # Return the full decrypted message


# Function to try every possible key (brute-force)
def brute_force(cipher_text):
    print("\n[+] Brute-force results:")
    for key in range(26):  # Try all possible key values from 0 to 25
        attempt = decrypt(cipher_text, key)  # Decrypt using current key
        print("Key " + str(key) + ": " + attempt)  # Print possible plaintext


# Main menu function to interact with the user
def main():
    while True:
        # Display options to the user
        print("\n====== Caesar Cipher Tool ======")
        print("1. Encrypt a message")
        print("2. Decrypt a message with key")
        print("3. Brute-force decrypt a message")
        print("4. Quit")

        # Get the user's choice
        choice = input("Select an option (1–4): ").strip()

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter the key (0–25): "))  # Convert input to an integer
            encrypted = encrypt(message, key)  # Call encryption function
            print("Encrypted message:", encrypted)

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            key = int(input("Enter the key used to encrypt (0–25): "))
            decrypted = decrypt(message, key)  # Call decryption function
            print("Decrypted message:", decrypted)

        elif choice == '3':
            message = input("Enter the message to brute-force decrypt: ")
            brute_force(message)  # Try all possible keys

        elif choice == '4':
            print("Exiting program. Goodbye!")  # Exit message
            break  # Exit the loop

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")  # Input validation

        if __name__ == "__main__":
            main()

