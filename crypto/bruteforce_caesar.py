

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def bruteforce_caesar(ciphertext):
    for shift in range(26):
        plaintext = caesar_cipher(ciphertext, shift)
        print(f"Shift {shift}: {plaintext}")

# Example usage
ciphertext = input("Enter the ciphertext: ")
bruteforce_caesar(ciphertext)

