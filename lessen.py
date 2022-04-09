numbers = [int(number) for number in input().split('; ')]

multiply = 1
for x in numbers:
    multiply *= x

print(multiply)
