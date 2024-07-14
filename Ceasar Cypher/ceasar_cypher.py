def encrypt(plain_text, key):
    """
    Function to encrypt a message using a simple Caesar cipher.

    Parameters:
    - plain_text: The original message to be encrypted.
    - key: The number of positions to shift each letter in the message.

    Returns:
    - The encrypted message.
    """
    cipher_text = ""  # Initialize an empty string for the encrypted message

    # Loop through each character in the plain text
    for char in plain_text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the ASCII offset ('A' for uppercase, 'a' for lowercase)
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Encrypt the character by shifting it by 'key' positions in the alphabet
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            cipher_text += encrypted_char  # Add the encrypted character to the cipher text
        else:
            cipher_text += char  # If the character is not a letter, add it unchanged

    return cipher_text  # Return the complete encrypted message

def decrypt(cipher_text, key):
    """
    Function to decrypt a message that was encrypted using a Caesar cipher.

    Parameters:
    - cipher_text: The encrypted message to be decrypted.
    - key: The number of positions each letter was shifted during encryption.

    Returns:
    - The original plain text message.
    """
    plain_text = ""  # Initialize an empty string for the decrypted message

    # Loop through each character in the cipher text
    for char in cipher_text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the ASCII offset ('A' for uppercase, 'a' for lowercase)
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Decrypt the character by shifting it back by 'key' positions in the alphabet
            decrypted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            plain_text += decrypted_char  # Add the decrypted character to the plain text
        else:
            plain_text += char  # If the character is not a letter, add it unchanged

    return plain_text  # Return the complete decrypted message

# Main program
while True:
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? Enter E or D (or Q to quit): ").upper()
    
    if choice == 'Q':
        print("Exiting program.")
        break

    if choice in ['E', 'D']:
        message = input("Enter your message: ")
        key = int(input("Enter the key (number of positions to shift): "))

        if choice == 'E':
            result = encrypt(message, key)
            print("Encrypted message:", result)
        else:
            result = decrypt(message, key)
            print("Decrypted message:", result)
    else:
        print("Invalid choice. Please enter E, D, or Q.")