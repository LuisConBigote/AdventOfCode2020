solution1, solution2 = 0, 0

boot_code = [line.strip() for line in open("../input/seven")]
boot_code = [(line.split()[0], int(line.split()[1])) for line in boot_code]

accumulator = 0
line_terminated = len(boot_code)

def execute(code, line):
    global accumulator
    operation, argument = code[line]
    if (operation == 'acc'):
        accumulator += argument
    if (operation == 'jmp'):
        line += argument - 1
    if (operation == 'nop'):
        pass
    line += 1
    return line

def checker(code):
    lines_executed = set()
    line = 0
    while line not in lines_executed:
        lines_executed.add(line)
        line = execute(code, line)
        if line == line_terminated:
            return line
    return line

checker(boot_code)
solution1 =  accumulator

for index, line in enumerate(boot_code):
    operation, argument = line
    accumulator = 0
    if operation == 'acc':
        continue

    newcode = boot_code.copy()
    if operation == 'nop':
        newcode[index] = 'jmp', newcode[index][1]
    else:
        newcode[index] = 'nop', newcode[index][1]

    if checker(newcode) == line_terminated:
        solution2 = accumulator
        break

print("First solution:", solution1)
print("Second solution:", solution2)
