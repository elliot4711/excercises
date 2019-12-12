import random
numbers = []

def randomlist(lenght):
    for _ in range(lenght):
        numbers.append(random.randint(0, 100))

randomlist(7)
print(numbers)
winning_number = random.randint(1, 100)
print(winning_number)

if winning_number in numbers:
    print("You won")
else:
    print("You lost")