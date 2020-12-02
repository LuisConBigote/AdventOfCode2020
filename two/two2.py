file = open("../input/two1")

counter = 0
l = []
for line in file:
    policy, password = line.strip().split(":")
    rang, letter = policy.split()
    rang = rang.split("-")

    first = password[int(rang[0])] == letter
    second = password[int(rang[1])] == letter

    if ((first and not second) or (not first and second)):
        counter = counter + 1

print(counter)
