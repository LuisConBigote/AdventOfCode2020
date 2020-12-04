matrix = [line.strip() for line in open("./input/three")]

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

res = 1

for slope in slopes:
    trees = 0
    x, y = 0, 0
    while y < len(matrix) - 1:
        x = (x + slope[0]) % len(matrix[0])
        y += slope[1]
        if matrix[y][x] == "#":
            trees += 1
    res *= trees

print(res)
