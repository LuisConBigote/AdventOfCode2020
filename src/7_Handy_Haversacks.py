file = [line.strip().rstrip('.') for line in open('../input/seven')]
file = [line.split('s contain ') for line in file]
file = [(bag, contained.strip('s').split(', ')) for bag, contained in file]

for line in file:
    bag, _cbags = line
    cbags = []
    if 'no other bag' not in cbags:
        for cbag in _cbags:
            cbags.append((cbag[:1], cbag[2:]))

    print(bag, cbags)


