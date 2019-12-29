

def load_journal_entries(lenght):
    with open('my_journal.txt', 'r') as f:
        lines = f.read().splitlines()
        first_line = lines[-lenght]
        second_line = lines[-(lenght-1)]
        third_line = lines[-(lenght-2)]
        return first_line + "," + second_line + "," + third_line

def silly_decrypt(encrypted_string, shift):
    decrypted_letter = []
    letters = []
    encrypted_letter = []
    encrypted_string = [char for char in encrypted_string]
    for y in range(len(encrypted_string)):
        encrypted_letter.append(ord(encrypted_string[y]))
        decrypted_letter.append(encrypted_letter[y] - shift)
        letters.append(chr(decrypted_letter[y]))
    
    letters = "".join(letters)
    return letters
    

    
def print_journal():
    encrypted_text = load_journal_entries(3)
    print(encrypted_text)
    decrypted_text = silly_decrypt(encrypted_text, 1)
    print(decrypted_text)
    decrypted_text = decrypted_text.replace("+", " ")
    print(decrypted_text)

print_journal()
