matrix =[]
def playfair(text, key):
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join(c for c in text.upper() if c.isalpha())
    key = key.upper().replace(" ", "")
    
    # Create 5x5 matrix
    matrix = create_matrix(key)
    
    # Split text into pairs
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    print(pairs)
    
    # Handle pairs with same letters
    pairs = handle_same_letters(pairs)
    
    # Encrypt pairs
    cipher = ""
    for pair in pairs:
        row1, col1 = get_position(matrix, pair[0])
        row2, col2 = get_position(matrix, pair[1])
        
        if row1 == row2:
            cipher += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            cipher += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            cipher += matrix[row1][col2] + matrix[row2][col1]
            
    return cipher

def create_matrix(key):
    matrix = []
    letters = [c for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
    for char in key + "".join(letters):
        if char not in matrix and char in letters:
            letters.remove(char)
            matrix.append(char)
    matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
    return matrix

def get_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j

def handle_same_letters(pairs):
    new_pairs = []
    for pair in pairs:
        if len(pair) == 2 and pair[0] == pair[1]:
            new_pairs.append(pair[0] + 'X')
        else:
            new_pairs.append(pair)
    if len(new_pairs[-1]) == 1:
        new_pairs[-1] += 'X'
    return new_pairs
def decrypt(text, key):
    # Create 5x5 matrix
    matrix = create_matrix(key)
    
    # Split text into pairs
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    
    # Decrypt pairs
    plain = ""
    for pair in pairs:
        row1, col1 = get_position(matrix, pair[0])
        row2, col2 = get_position(matrix, pair[1])
        
        if row1 == row2:
            plain += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plain += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            plain += matrix[row1][col2] + matrix[row2][col1]
    
    return plain


print(playfair(" HOLY", "PLAYFAIR"))
print(decrypt("GQAF", "PLAYFAIR"))