
def read_file(filename):
    with open(filename) as file:
        return [[char for char in line.strip('\n')] for line in file]

def occupied_adjacent_seats(grid, row, pos, height, width):
    return (1 if row - 1 >= 0 and pos - 1 >= 0 and grid[row - 1][pos - 1] == '#' else 0) + \
        (1 if row - 1 >= 0 and grid[row - 1][pos] == '#' else 0) + \
        (1 if row - 1 >= 0 and pos + 1 < width and grid[row - 1][pos + 1] == '#' else 0) + \
        (1 if pos - 1 >= 0 and grid[row][pos - 1] == '#' else 0) + \
        (1 if pos + 1 < width and grid[row][pos + 1] == '#' else 0) + \
        (1 if row + 1 < height and pos - 1 >= 0 and grid[row + 1][pos - 1] == '#' else 0) + \
        (1 if row + 1 < height and grid[row + 1][pos] == '#' else 0) + \
        (1 if row + 1 < height and pos + 1 < width and grid[row + 1][pos + 1] == '#' else 0)

def occupied_visible_seats(grid, row, pos, height, width):
    occupied = 0
    i = 0
    while True:
        i -= 1
        if row + i >= 0:
            if grid[row + i][pos] == '#':
                occupied += 1
                break
            elif grid[row + i][pos] == 'L':
                break
        else:
            break
    i = 0
    j = 0
    while True:
        i -= 1
        j += 1
        if row + i >= 0 and pos + j < width:
            if grid[row + i][pos + j] == '#':
                occupied += 1
                break
            elif grid[row + i][pos + j] == 'L':
                break
        else:
            break
    j = 0
    while True:
        j += 1
        if pos + j < width:
            if grid[row][pos + j] == '#':
                occupied += 1
                break
            elif grid[row][pos + j] == 'L':
                break
        else:
            break
    i = 0
    j = 0
    while True:
        i += 1
        j += 1
        if row + i < height and pos + j < width:
            if grid[row + i][pos + j] == '#':
                occupied += 1
                break
            elif grid[row + i][pos + j] == 'L':
                break
        else:
            break
    i = 0
    while True:
        i += 1
        if row + i < height:
            if grid[row + i][pos] == '#':
                occupied += 1
                break
            elif grid[row + i][pos] == 'L':
                break
        else:
            break
    i = 0
    j = 0
    while True:
        i += 1
        j -= 1
        if row + i < height and pos + j >= 0:
            if grid[row + i][pos + j] == '#':
                occupied += 1
                break
            elif grid[row + i][pos + j] == 'L':
                break
        else:
            break
    j = 0
    while True:
        j -= 1
        if pos + j >= 0:
            if grid[row][pos + j] == '#':
                occupied += 1
                break
            elif grid[row][pos + j] == 'L':
                break
        else:
            break
    i = 0
    j = 0
    while True:
        i -= 1
        j -= 1
        if row + i >= 0 and pos + j >= 0:
            if grid[row + i][pos + j] == '#':
                occupied += 1
                break
            elif grid[row + i][pos + j] == 'L':
                break
        else:
            break
    return occupied
    
def occupied_seats(grid):
    return sum([sum([1 if char == '#' else 0 for char in row]) for row in grid])

def iterate(grid, part):
    new_grid = [line[:] for line in grid[:]]
    height = len(grid)
    width = len(grid[0])
    changed = False
    
    for row in range(0, height):
        for pos in range(0, width):
            if grid[row][pos] == 'L':
                if part == 1:
                    if occupied_adjacent_seats(grid, row, pos, height, width) == 0:
                        changed = True
                        new_grid[row][pos] = '#'
                elif part == 2:
                    if occupied_visible_seats(grid, row, pos, height, width) == 0:
                        changed = True
                        new_grid[row][pos] = '#'
            elif grid[row][pos] == '#':
                if part == 1:
                    if occupied_adjacent_seats(grid, row, pos, height, width) >= 4:
                        changed = True
                        new_grid[row][pos] = 'L'
                elif part == 2:
                    if occupied_visible_seats(grid, row, pos, height, width) >= 5:
                        changed = True
                        new_grid[row][pos] = 'L'
                        
    return new_grid, changed

grid = read_file('testinput.txt')
i = 0
while True:
    grid, changed = iterate(grid, 1)
    i += 1
    if not changed:
        print(f'nothing happened on iteration {i}')
        print(occupied_seats(grid))
        break

grid = read_file('input.txt')
i = 0
while True:
    grid, changed = iterate(grid, 1)
    i += 1
    if not changed:
        print(f'nothing happened on iteration {i}')
        print(occupied_seats(grid))
        break

grid = read_file('testinput.txt')
i = 0
while True:
    grid, changed = iterate(grid, 2)
    i += 1
    if not changed:
        print(f'nothing happened on iteration {i}')
        print(occupied_seats(grid))
        break

grid = read_file('input.txt')
i = 0
while True:
    grid, changed = iterate(grid, 2)
    i += 1
    if not changed:
        print(f'nothing happened on iteration {i}')
        print(occupied_seats(grid))
        break


