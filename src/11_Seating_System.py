import copy
inp = [list(line.strip()) for line in open("../input/eleven")]

def change_cell(y,x, cells, solution=1):
    cell = cells[y][x]
    in_sight = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i == j == 0:
                continue
            nx, ny = i, j
            if solution == 1:
                if 0 <= x+nx < len(cells[0]) and 0 <= y+ny< len(cells):
                    in_sight.append(cells[y+ny][x+nx])
            else:
                while 0 <= x + nx < len(cells[0]) and 0 <= y + ny < len(cells):
                    ncell = cells[y+ny][x+nx]
                    if ncell != '.':
                        in_sight.append(ncell)
                        break
                    else:
                        nx += i
                        ny += j

    taken = in_sight.count('#')
    if cell == 'L':
        if taken == 0:
            return '#'
        else:
            return 'L'
    elif cell == '#':
        if (solution == 1 and taken >= 4) or (solution == 2 and taken >= 5):
            return 'L'
        else:
            return '#'
    else:
        return '.'

def next_stage(stage, solution=1):
    next_stage = copy.deepcopy(stage)
    for x in range(len(stage[0])):
        for y in range(len(stage)):
            next_stage[y][x] = change_cell(y,x,stage,solution=solution)

    return next_stage

def stabilize(start_grid, solution=1):
    last_stage = []
    stage = copy.deepcopy(start_grid)
    while last_stage != stage:
        stage, last_stage = next_stage(stage,solution=solution), stage
    return stage

stage = stabilize(inp, solution=1)
solution1 = sum([sum([1 for char in line if char == '#']) for line in stage])

stage = stabilize(inp, solution=2)
solution2 = sum([sum([1 for char in line if char == '#']) for line in stage])

print('First solution:', solution1)
print('Second solution:', solution2)
