"""
def divisible_by(number_1, number_2):
    x = number_1/number_2
    x = float(x)
    return x.is_integer()

print(divisible_by(1,2))
print(divisible_by(4,2))
"""
def divisible(number_1, number_2):
    if number_1 % number_2 !=0:
        return False
    else:
        return True

for y in range(1, 1001):
    if divisible(y, 7):
        if not divisible(y, 2):
            print(y)
