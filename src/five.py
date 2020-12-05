def convert(string):
    return string.replace('F','0').replace('B','1').replace('R','1').replace('L','0')

seats = [line.rstrip() for line in open("./input/five")]

IDs = []
for seat in seats:
    row = int(convert(seat[:-3]),base=2)
    column = int(convert(seat[-3:]),base=2)
    IDs.append(row * 8 + column)

first_s = sorted(IDs, reverse=True)[0]
second_s = list(set(range(first_s - 1)).difference(set(IDs)))[-1]

print("First solution: ", first_s)
print("Second solution: ", second_s)
