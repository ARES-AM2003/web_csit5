import numpy as np
from sympy import Matrix

def mod_inverse_matrix(matrix, modulus):
    sympy_matrix = Matrix(matrix)
    return np.array(sympy_matrix.inv_mod(modulus)).astype(int)

def clean_text(text):
    text = text.replace(" ", "").upper()
    return "".join([char for char in text if char.isalpha()])

def pad_text(text, block_size):
    while len(text) % block_size != 0:
        text += 'X'
    return text

def text_to_matrix(text, n):
    text_matrix = [ord(char) - 65 for char in text]
    return np.array(text_matrix).reshape((-1, n))

def matrix_to_text(matrix):
    return "".join([chr(num + 65) for num in matrix.flatten()])

def encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    n = key.shape[0]
    plaintext = pad_text(plaintext, n)
    plaintext_matrix = text_to_matrix(plaintext, n)
    
    ciphertext_matrix = np.dot(key, plaintext_matrix.T) % 26
    ciphertext = matrix_to_text(ciphertext_matrix.T)
    
    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = clean_text(ciphertext)
    n = key.shape[1]
    ciphertext_matrix = text_to_matrix(ciphertext, n)
    
    key_inv = mod_inverse_matrix(key, 26)
    plaintext_matrix = np.dot(key_inv, ciphertext_matrix.T) % 26
    plaintext = matrix_to_text(plaintext_matrix.T)
    
    return plaintext

if __name__ == "__main__":
    key = np.array([[17, 17, 5],
                    [21, 18, 21],
                    [2, 2, 19]])
    
    plaintext = "Pay more money"
    ciphertext = encrypt(plaintext, key)
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    
    decrypted = decrypt(ciphertext, key)
    print(f"Decrypted: {decrypted}")
