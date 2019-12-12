cities = ["Stockholm", "New York", "Tokyo", "Berlin"]

def contains(list, string):
    if string in list:
        return True
    if string not in list:
        return False
    
print(contains(cities, "Stockholm"))
print(contains(cities, "New Jersey"))
