def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift)

def decrypt(text, shift):
    return caesar_cipher(text, -shift)
