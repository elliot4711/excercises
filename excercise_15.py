def reverse(string): 
    if len(string) == 0: 
        return string 
    else: 
        return reverse(string[1:]) + string[0]

def is_palindrom(string):
    if string == reverse(string):
        return True
    else:
        return False

print(is_palindrom("anna"))
print(is_palindrom("elliot"))