import string ,random

alphabet = string.ascii_lowercase
key=list(alphabet)
random.shuffle(key)
key="".join(key)
def encrypt(plaintext):
      
    plaintext = plaintext.lower()
    
    cipher_map = dict(zip(alphabet, key))
    print(cipher_map)
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ciphertext += cipher_map[char]
        else:
            ciphertext += char
    return ciphertext
def decrypt(ciphertext):
    
    ciphertext = ciphertext.lower()
    
    cipher_map = dict(zip(key, alphabet))
    print(cipher_map)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += cipher_map[char]
        else:
            plaintext += char
    return plaintext
print(encrypt("Hello World"))
print(decrypt(encrypt("Hello World")))