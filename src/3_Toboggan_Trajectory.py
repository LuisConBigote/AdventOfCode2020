file = open("./input/three")

matrix = []

for line in file:
    matrix.append(line.strip())

rA = rB = rC = rD = rE = 0
cA = cB = cC = cD = cE = 0

def check(spot):
    if spot == "#":
        return 1
    else:
        return 0

for count, row in enumerate(matrix):
    if count % 2 == 0:
        spot = row[(rE) % len(row)]
        rE += 1
        cE += check(spot)

    spotA = row[(rA) % len(row)]
    cA += check(spotA)
    rA += 1
    spotB = row[(rB) % len(row)]
    cB += check(spotB)
    rB += 3
    spotC = row[(rC) % len(row)]
    cC += check(spotC)
    rC += 5
    spotD = row[(rD) % len(row)]
    cD += check(spotD)
    rD += 7

print(cA*cB*cC*cD*cE)
