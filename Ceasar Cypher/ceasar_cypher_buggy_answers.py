def encrypt(plain_text, key):
    cipher_text = ""

    for char in plain_text:
        if char.isalpha():
            ascii_offset = ord('a') if char.isupper() else ord('a')  # BUG: should be ord('A') for uppercase
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            cipher_text += encrypted_char
        else:
            cipher_text = char  # BUG: should be += to append non-letter characters

    return ciphertext  # BUG: 'ciphertext' is undefined; should be 'cipher_text'


def decrypt(cipher_text, key):
    plain_text = ""

    for char in cipher_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper else ord('a')  # BUG: missing () in 'isupper'
            decrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)  # BUG: should subtract key
            plain_text += decrypted_char
        else:
            plain_text += char

    return plain_text


def brute_force(cipher_text):
    print("\n[+] Brute-force results:")
    for key in range(27):  # BUG: should be range(26)
        attempt = decrypt(cipher_text, key)
        print("Key " + str(key) + ": " + attempt)


def main()  # BUG: missing colon
    while True:
        print("\n====== Caesar Cipher Tool ======")
        print("1. Encrypt a message")
        print("2. Decrypt a message with key")
        print("3. Brute-force decrypt a message")
        print("4. Quit")

        choice = input("Select an option (1–4): ").strip()

        if choice == 1:  # BUG: input() returns string, should compare to '1'
            message = input("Enter the message to encrypt: ")
            key = input("Enter the key (0–25): ")  # BUG: input not cast to int
            encrypted = encrypt(message, key)
            print("🔒 Encrypted message:", encrypted)

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            key = int(input("Enter the key used to encrypt (0–25): "))
            decrypted = decrypt(message, key)
            print("🔓 Decrypted message:", decrypted)

        elif choice == '3':
            message = input("Enter the message to brute-force decrypt: ")
            brute_force(message)

        elif choice == '4':
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 4.")

