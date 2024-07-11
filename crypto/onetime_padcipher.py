
import random

def generate_key(length):
    return [random.randint(0, 25) for _ in range(length)]

def one_time_pad(text, key, mode):
    result = ''
    for i in range(len(text)):
        char = text[i].upper()
        shift = key[i]
        if char.isalpha():
            if mode == 'encrypt':
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif mode == 'decrypt':
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += char
    return result

# Example usage
key = generate_key(len('hello'))
print(f"Generated Key: {key}")

encrypted_text = one_time_pad('hello', key, 'encrypt')
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = one_time_pad(encrypted_text, key, 'decrypt')
print(f"Decrypted Text: {decrypted_text}")
