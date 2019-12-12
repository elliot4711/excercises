import random
numbers = []

def randomlist(lenght):
    for _ in range(lenght):
        numbers.append(random.randint(0, 100))

randomlist(10)
print(numbers)