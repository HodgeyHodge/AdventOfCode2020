
def read_file(filename):
    with open(filename) as file:
        return [line
            .strip('\n')
            .replace('ne', '1')
            .replace('nw', '2')
            .replace('sw', '4')
            .replace('se', '5')
            .replace('e', '0')
            .replace('w', '3')
        for line in file]

def enumerate_walks(walks):
    flips = {}
    for walk in walks:
        flip = [0, 0]
        for char in walk:
            if char == '0':
                flip[1] += 1
            elif char == '1':
                flip[0] += 1
            elif char == '2':
                flip[0] += 1
                flip[1] -= 1
            elif char == '3':
                flip[1] -= 1
            elif char == '4':
                flip[0] -= 1
            elif char == '5':
                flip[0] -= 1
                flip[1] += 1
        if tuple(flip) not in flips:
            flips[tuple(flip)] = 1
        else:
            flips[tuple(flip)] += 1
    return flips

def neighbours(coord):
    return [
        tuple([coord[0], coord[1] + 1]),
        tuple([coord[0] + 1, coord[1]]),
        tuple([coord[0] + 1, coord[1] - 1]),
        tuple([coord[0], coord[1] - 1]),
        tuple([coord[0] - 1, coord[1]]),
        tuple([coord[0] - 1, coord[1] + 1])
    ]

def prepopulate_white_tiles(flips):
    new_flips = {}
    for flip in flips:
        for n in neighbours(flip):
            if n not in flips:
                new_flips[n] = 0
    return flips | new_flips

def black_neighbour_count(flips, coord):
    count = 0
    for t in neighbours(coord):
        if t in flips and flips[t] % 2 == 1:
            count += 1
    return count

def evolve(flips):
    flips = prepopulate_white_tiles(flips)
    new_flips = flips.copy()
    for k, v in flips.items():
        if v % 2 == 1 and black_neighbour_count(flips, k) not in [1, 2]:
            new_flips[k] += 1
        elif v % 2 == 0 and black_neighbour_count(flips, k) == 2:
            new_flips[k] += 1
    return new_flips

print('Test Data')

walks = read_file('testinput.txt')
flips = enumerate_walks(walks)
print(len([k for k, v in flips.items() if v % 2 == 1]))

for i in range(0, 100):
    flips = evolve(flips)
print(len([k for k, v in flips.items() if v % 2 == 1]))

print('Live Data')

walks = read_file('input.txt')
flips = enumerate_walks(walks)
print(len([k for k, v in flips.items() if v % 2 == 1]))

for i in range(0, 100):
    flips = evolve(flips)
print(len([k for k, v in flips.items() if v % 2 == 1]))











