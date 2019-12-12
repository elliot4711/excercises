def divisible_by_five(number):
    x = number/5
    x = float(x)
    return x.is_integer()

print(divisible_by_five(5))
print(divisible_by_five(7))
