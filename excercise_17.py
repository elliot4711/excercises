import random
numbers = []

def randomlist(lenght):
    for _ in range(lenght):
        numbers.append(random.randint(0, 100))

randomlist(7)
print(numbers)
winning_number = random.randint(1, 100)
print(winning_number)



def play(money):
    money = money - 5
    if winning_number in numbers:
        print("You won")
        money = money + 30
        print(money)
        return money

    if winning_number not in numbers:
        print("You lost")
        print(money)
        return money
        


balance = play(50)
balance = play(balance)