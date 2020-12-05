def convert(string):
    return string.replace('F','0').replace('B','1').replace('R','1').replace('L','0')

seats = [line.rstrip() for line in open("./input/five")]

IDs = []
for seat in seats:
    row = int(convert(seat[:-3]),base=2)
    column = int(convert(seat[-3:]),base=2)
    IDs.append(row * 8 + column)

print(set(range(10000)).difference(set(IDs)))
