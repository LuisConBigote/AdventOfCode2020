inp = sorted([int(line.rstrip()) for line in open("../input/ten")])

hig = inp[-1]
aux = {hig: 1}

def recursive(n):
    if n in aux:
        return aux[n]
    else:
        res = 0
        for i in range(1,4):
            if (n + i <= hig) and (n + i in inp):
                res += recursive(n + i)
        aux[n] = res
        return res

print(recursive(0))
