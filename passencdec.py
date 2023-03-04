def encrypt(password, shift):
    encrypted = ""
    for char in password:
        if char.isalpha():
            char_code = ord(char) + shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            encrypted += chr(char_code)
        else:
            encrypted += char
    return encrypted

def decrypt(password, shift):
    return encrypt(password, -shift)

password = input("Enter your password: ")

while True:
    choice = input("Enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit: ")
    if choice == 'E':
        shift = int(input("Enter shift value (0-25): "))
        encrypted = encrypt(password, shift)
        print(f"Encrypted password: {encrypted}")
    elif choice == 'D':
        shift = int(input("Enter shift value (0-25): "))
        decrypted = decrypt(password, shift)
        print(f"Decrypted password: {decrypted}")
    elif choice == 'Q':
        break
    else:
        print("Invalid choice. Please try again.")