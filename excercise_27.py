from excercise_26 import print_journal
from excercise_26 import load_journal_entries
from excercise_24 import save_journal_entry

def show_menu():
    ans = input("Would you like to add a new journal entry, view your latest yournal entry, or quit the program? " )
    if ans == "new":
        ans = input("What would you like to enter into your journal? ")
        save_journal_entry(ans)
    if ans == "view":
        print_journal()
    else:
        quit

show_menu()

