def divisible_by(number_1, number_2):
    x = number_1/number_2
    x = float(x)
    return x.is_integer()

print(divisible_by(1,2))
print(divisible_by(4,2))