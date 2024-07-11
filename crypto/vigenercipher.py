def vigenere_cipher(text, key, mode):
    """
    Encrypts or decrypts the given text using the Vigenere cipher with the provided key.
    
    Args:
        text (str): The text to be encrypted or decrypted.
        key (str): The key to be used for encryption/decryption.
        mode (str): 'encrypt' or 'decrypt' to specify the operation.
        
    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key.upper()]
    
    for i, char in enumerate(text):
        if char.isalpha():
            char_as_int = ord(char.upper())
            shift = key_as_int[i % key_length]
            if mode == 'encrypt':
                result += chr((char_as_int + shift - 2 * ord('A')) % 26 + ord('A'))
            else:
                result += chr((char_as_int - shift) % 26 + ord('A'))
        else:
            result += char
            
    return result
print(vigenere_cipher('hello', 'key', 'encrypt'))
print(vigenere_cipher(vigenere_cipher('hello', 'key', 'encrypt'), 'key', 'decrypt'))