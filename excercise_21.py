
def silly_encrypt(string):
    encrypted_letter = []
    letters = []
    string = [char for char in string]
    for y in range(len(string)):
        encrypted_letter.append(ord(string[y]))
        encrypted_letter[y] = encrypted_letter[y] + 1
        letters.append(chr(encrypted_letter[y]))

    letters = "".join(letters)
    return letters
    
    
silly_encrypt("elliot")

