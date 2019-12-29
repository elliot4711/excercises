from excercise_21 import silly_encrypt
from excercise_24 import save_journal_entry

def add_journal_entry():
    ans = input("How was your day? ")
    ans = silly_encrypt(ans)
    save_journal_entry(ans)
    ans = input("Did you do anything fun? ")
    ans = silly_encrypt(ans)
    save_journal_entry(ans)
    ans = input("Did your mom make you spaghetti? ")
    ans = silly_encrypt(ans)
    save_journal_entry(ans)

add_journal_entry()
