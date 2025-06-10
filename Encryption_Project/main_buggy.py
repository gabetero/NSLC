def encrypt(plain_text, key):
    ciphertext = ""

    for ch in plain_text:
        if ch.isalpha():
            offset = ord('a') if ch.isupper() else ord('a')
            new_char = chr((ord(ch) - offset + key) % 26 + offset)
            ciphertext + new_char
        else:
            ciphertext =+ ch

    return cipher_text


def decrypt(ciphertext, shift):
    plain_text = ""

    for ch in ciphertext:
        if ch.isalpha:
            offset = ord('A') if ch.isupper else ord('a')
            new_char = chr((ord(ch) - offset + shift) % 26 + offset)
            plain_text.append(new_char)
        else:
            plain_text += ch

    return plaintext


def brute_force(ciphertext):
    print("\n[+] Brute-force Results:")
    for i in range(0, 26 + 1):
        possible = decrypt(ciphertext, i)
        print(f"Try {i}: {possible}")


def menu():
    loop = True
    while loop:
        print("===== Caesar Tool =====")
        print("Encrypt - 1")
        print("Decrypt - 2")
        print("Brute Force - 3")
        print("Exit - 4")

        user_input = input("Choice: ")

        if user_input == 1:
            msg = input("Message: ")
            k = input("Key: ")
            result = encrypt(msg, k)
            print("Result:", result)

        elif user_input == '2':
            txt = input("Encrypted: ")
            shift = int(input("Key: "))
            print(decrypt(txt, shift))

        elif user_input == '3':
            ct = input("Enter message: ")
            brute_force(ct)

        elif user_input == 4:
            loop = False
            print("Done.")

        else:
            print("Wrong input.")


if __name__ == "__main__":
    menu()
