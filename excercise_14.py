foods = ["taco", "pizza", "Mom's spaghetti", "IKEA MEATBALLS DALAHORSE FTW", "taco"]
not_foods = ["shoes", "fox", "mom", "warlock"]
def has_equal_ends(list):
    x = len(list)
    if list[0] == list[x-1]:
        return True
    else:
        return False

print(has_equal_ends(foods))
print(has_equal_ends(not_foods))