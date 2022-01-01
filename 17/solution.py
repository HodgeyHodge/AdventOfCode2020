
from itertools import product

def iterate(active_cells):
    turn_on = set()
    turn_off = set()
    for cell in active_cells:
        if len(adjacent_cells(cell).intersection(active_cells)) not in [3, 4]:
            turn_off.add(cell)
        for adjacent_cell in adjacent_cells(cell):
            if adjacent_cell not in active_cells:
                if len(adjacent_cells(adjacent_cell).intersection(active_cells)) == 3:
                    turn_on.add(adjacent_cell)
    return active_cells.union(turn_on).difference(turn_off)

print('Part one')

def adjacent_cells(cell):
    return set(product(range(cell[0] - 1, cell[0] + 2), range(cell[1] - 1, cell[1] + 2), range(cell[2] - 1, cell[2] + 2)))

print('Test data')

active_cells = set([(0, 1, 0), (1, 2, 0), (2, 0, 0), (2, 1, 0), (2, 2, 0)])

for _ in range(0, 6):
    active_cells = iterate(active_cells)

print(len(active_cells))

print('Live data')

active_cells = set([
    (0,4,0), (0,5,0), (0,6,0),
    (1,0,0), (1,4,0), (1,5,0), (1,6,0), (1,7,0),
    (2,0,0), (2,1,0), (2,3,0), (2,5,0), (2,6,0), (2,7,0),
    (3,2,0), (3,4,0),
    (4,0,0), (4,1,0), (4,3,0), (4,5,0), (4,7,0),
    (5,0,0), (5,2,0), (5,3,0), (5,4,0), (5,5,0), (5,6,0), (5,7,0),
    (6,2,0), (6,5,0), (6,7,0),
    (7,0,0), (7,1,0), (7,2,0), (7,3,0), (7,4,0), (7,5,0), (7,7,0)
])

for _ in range(0, 6):
    active_cells = iterate(active_cells)

print(len(active_cells))

print('Part two')

def adjacent_cells(cell):
    return set(product(range(cell[0] - 1, cell[0] + 2), range(cell[1] - 1, cell[1] + 2), range(cell[2] - 1, cell[2] + 2), range(cell[3] - 1, cell[3] + 2)))

print('Test data')

active_cells = set([(0, 1, 0, 0), (1, 2, 0, 0), (2, 0, 0, 0), (2, 1, 0, 0), (2, 2, 0, 0)])

for _ in range(0, 6):
    active_cells = iterate(active_cells)

print(len(active_cells))

print('Live data')

active_cells = set([
    (0,4,0,0), (0,5,0,0), (0,6,0,0),
    (1,0,0,0), (1,4,0,0), (1,5,0,0), (1,6,0,0), (1,7,0,0),
    (2,0,0,0), (2,1,0,0), (2,3,0,0), (2,5,0,0), (2,6,0,0), (2,7,0,0),
    (3,2,0,0), (3,4,0,0),
    (4,0,0,0), (4,1,0,0), (4,3,0,0), (4,5,0,0), (4,7,0,0),
    (5,0,0,0), (5,2,0,0), (5,3,0,0), (5,4,0,0), (5,5,0,0), (5,6,0,0), (5,7,0,0),
    (6,2,0,0), (6,5,0,0), (6,7,0,0),
    (7,0,0,0), (7,1,0,0), (7,2,0,0), (7,3,0,0), (7,4,0,0), (7,5,0,0), (7,7,0,0)
])

for _ in range(0, 6):
    active_cells = iterate(active_cells)

print(len(active_cells))