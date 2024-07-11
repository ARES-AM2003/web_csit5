def vernam_cipher(text, key, mode):
    """
    Encrypt or decrypt text using the Vernam cipher with the given key.
    """
    result = ""
    key = key.upper()  # Ensure the key is uppercase
    text = text.upper()  # Ensure the text is uppercase for consistency
    
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            if mode == 'encrypt':
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif mode == 'decrypt':
                result += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))  # Added +26 to ensure non-negative result
        else:
            result += char
    return result

# Example usage
plaintext = "HELLO"
key = "XMCKL"

encrypted_text = vernam_cipher(plaintext, key, 'encrypt')
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = vernam_cipher(encrypted_text, key, 'decrypt')
print(f"Decrypted Text: {decrypted_text}")
