inp = [int(line.strip()) for line in open("../input/nine")]

def checksum(array:list, x:int):
    d = {}
    for n in array:
        if n not in d:
            d[x-n] = n
        else:
            return True
    return False

preamble, stream = inp[:25], inp[25:]
while checksum(preamble, stream[0]):
    preamble.pop(0)
    preamble.append(stream.pop(0))
solution1 = stream[0]

data = inp[25:]
for n in range(len(data)):
    for m in range(n, len(data)):
        if sum(data[n:m]) == solution1 and n != m - 1:
            c = sorted(data[n:m])
            solution2 = c[0] + c[-1]

print("First solution:", solution1)
print("Second solution:", solution2)
