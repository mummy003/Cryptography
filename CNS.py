def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted
plaintext = input("Enter your message: ")
key = int(input("Enter shift key (e.g., 3): "))
cipher_text = encrypt(plaintext, key)
print("Encrypted message:", cipher_text)