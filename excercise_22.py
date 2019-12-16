
def save_journal_entry(entry):
    my_file = open("/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/excercises/my_journal.txt","a")#append mode 
    my_file.write(entry +  "\n") 
    my_file.close() 

save_journal_entry("Today was a day, moms spaghetti")