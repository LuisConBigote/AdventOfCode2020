file = open("./input/two1")

counter = 0
l = []
for line in file:
    policy, password = line.strip().split(":")
    rang, letter = policy.split()
    rang = rang.split("-")

    ocurrences = password.count(letter)
    if (ocurrences >= int(rang[0]) and ocurrences <= int(rang[1])):
        counter = counter + 1

print(counter)
