file = open("./input/two")

counterFirst = 0
counterSecond = 0
l = []

for line in file:
    policy, password = line.strip().split(":")
    n_range, character = policy.split()
    n_range = n_range.split("-")
    first(password, character, n_range)
    second(password, character, n_range)

def first(passw, char, rang):
    n = password.count(character)
    if (n >= int(rang[0]) and n <= int(rang[1])):
        counterFirst = counterFirst + 1

def second(passw, char, rang):
    fBool = passw[int(rang[0])] == char
    sBool = passw[int(rang[1])] == char

    if ((fBool and not sBool) or (not fBool and sBool)):
        counterSecond = counterSecond + 1

print(counterFirst)
print(counterSecond)
