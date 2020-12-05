file = [int(line.strip()) for line in open("./input/one")]

for num1 in file:
    for num2 in file:
        for num3 in file:
            if (num1 + num2 + num3) == 2020:
                solution2 = num1*num2*num3

        if (num1+num2) == 2020:
            solution1 = num1*num2

print("First solution ", solution1)
print("Second solution ", solution2)
