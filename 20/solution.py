
from math import sqrt
from functools import reduce

def analyze_tile(raw_tile):
    return raw_tile[0], ''.join([raw_tile[i][9] for i in range(0, 10)]), raw_tile[9], ''.join([raw_tile[i][0] for i in range(0, 10)]), [''.join([raw_tile[i][j] for j in range(1, 9)]) for i in range(1, 9)]
    
def read_file(filename):
    with open(filename) as file:
        dict = {}
        raw_tile = []
        for line in file:
            if line.startswith('Tile '):
                current_tile = int(line.replace('Tile ', '').replace(':\n', ''))
            elif len(line) == 1:
                dict[current_tile] = analyze_tile(raw_tile)
                raw_tile = []
            else:
                raw_tile.append(line.strip('\n'))
        dict[current_tile] = analyze_tile(raw_tile)
    return dict

def flip_v(tile):
    return tile[2], tile[1][::-1], tile[0], tile[3][::-1], tile[4][::-1]

def flip_h(tile):
    return tile[0][::-1], tile[3], tile[2][::-1], tile[1], [line[::-1] for line in tile[4]]

def rot_90(tile):
    return tile[1], tile[2][::-1], tile[3], tile[0][::-1], [''.join([tile[4][i][j] for i in range(0, 8)]) for j in range(7, -1, -1)]

def rot_270(tile):
    return tile[3][::-1], tile[0], tile[1][::-1], tile[2], [''.join([tile[4][i][j] for i in range(7, -1, -1)]) for j in range(0, 8)]

def match_up(tiles):
    arbitrary_tile = min(tiles)
    true_tiles = {(0, 0): [*tiles[arbitrary_tile], min(tiles)]}
    tiles.pop(arbitrary_tile)

    while len(tiles) > 0:
        for tile_key, tile_value in true_tiles.items():
            for candidate_key, candidate_value in tiles.items():
                #direct
                if tile_value[0] == candidate_value[2]:
                    true_tiles.update({(tile_key[0] - 1, tile_key[1]): [*candidate_value, candidate_key]})
                elif tile_value[1] == candidate_value[3]:
                    true_tiles.update({(tile_key[0], tile_key[1] + 1): [*candidate_value, candidate_key]})
                elif tile_value[2] == candidate_value[0]:
                    true_tiles.update({(tile_key[0] + 1, tile_key[1]): [*candidate_value, candidate_key]})
                elif tile_value[3] == candidate_value[1]:
                    true_tiles.update({(tile_key[0], tile_key[1] - 1): [*candidate_value, candidate_key]})
                #direct with a twist
                elif tile_value[0] == candidate_value[2][::-1]:
                    true_tiles.update({(tile_key[0] - 1, tile_key[1]): [*flip_h(candidate_value), candidate_key]})
                elif tile_value[1] == candidate_value[3][::-1]:
                    true_tiles.update({(tile_key[0], tile_key[1] + 1): [*flip_v(candidate_value), candidate_key]})
                elif tile_value[2] == candidate_value[0][::-1]:
                    true_tiles.update({(tile_key[0] + 1, tile_key[1]): [*flip_h(candidate_value), candidate_key]})
                elif tile_value[3] == candidate_value[1][::-1]:
                    true_tiles.update({(tile_key[0], tile_key[1] - 1): [*flip_v(candidate_value), candidate_key]})
                #same side
                elif tile_value[0] == candidate_value[0]:
                    true_tiles.update({(tile_key[0] - 1, tile_key[1]): [*flip_v(candidate_value), candidate_key]})
                elif tile_value[1] == candidate_value[1]:
                    true_tiles.update({(tile_key[0], tile_key[1] + 1): [*flip_h(candidate_value), candidate_key]})
                elif tile_value[2] == candidate_value[2]:
                    true_tiles.update({(tile_key[0] + 1, tile_key[1]): [*flip_v(candidate_value), candidate_key]})
                elif tile_value[3] == candidate_value[3]:
                    true_tiles.update({(tile_key[0], tile_key[1] - 1): [*flip_h(candidate_value), candidate_key]})
                #same side with a twist
                elif tile_value[0] == candidate_value[0][::-1]:
                    true_tiles.update({(tile_key[0] - 1, tile_key[1]): [*flip_h(flip_v(candidate_value)), candidate_key]})
                elif tile_value[1] == candidate_value[1][::-1]:
                    true_tiles.update({(tile_key[0], tile_key[1] + 1): [*flip_h(flip_v(candidate_value)), candidate_key]})
                elif tile_value[2] == candidate_value[2][::-1]:
                    true_tiles.update({(tile_key[0] + 1, tile_key[1]): [*flip_h(flip_v(candidate_value)), candidate_key]})
                elif tile_value[3] == candidate_value[3][::-1]:
                    true_tiles.update({(tile_key[0], tile_key[1] - 1): [*flip_h(flip_v(candidate_value)), candidate_key]})
                #off clockwise
                elif tile_value[0] == candidate_value[3]:
                    true_tiles.update({(tile_key[0] - 1, tile_key[1]): [*rot_90(candidate_value), candidate_key]})
                elif tile_value[1] == candidate_value[0]:
                    true_tiles.update({(tile_key[0], tile_key[1] + 1): [*flip_v(rot_90(candidate_value)), candidate_key]})
                elif tile_value[2] == candidate_value[1]:
                    true_tiles.update({(tile_key[0] + 1, tile_key[1]): [*rot_90(candidate_value), candidate_key]})
                elif tile_value[3] == candidate_value[2]:
                    true_tiles.update({(tile_key[0], tile_key[1] - 1): [*flip_v(rot_90(candidate_value)), candidate_key]})
                #off clockwise with a twist
                elif tile_value[0] == candidate_value[3][::-1]:
                    true_tiles.update({(tile_key[0] - 1, tile_key[1]): [*flip_h(rot_90(candidate_value)), candidate_key]})
                elif tile_value[1] == candidate_value[0][::-1]:
                    true_tiles.update({(tile_key[0], tile_key[1] + 1): [*rot_90(candidate_value), candidate_key]})
                elif tile_value[2] == candidate_value[1][::-1]:
                    true_tiles.update({(tile_key[0] + 1, tile_key[1]): [*flip_h(rot_90(candidate_value)), candidate_key]})
                elif tile_value[3] == candidate_value[2][::-1]:
                    true_tiles.update({(tile_key[0], tile_key[1] - 1): [*rot_90(candidate_value), candidate_key]})
                #off anti-clockwise
                elif tile_value[0] == candidate_value[1]:
                    true_tiles.update({(tile_key[0] - 1, tile_key[1]): [*flip_h(rot_270(candidate_value)), candidate_key]})
                elif tile_value[1] == candidate_value[2]:
                    true_tiles.update({(tile_key[0], tile_key[1] + 1): [*rot_270(candidate_value), candidate_key]})
                elif tile_value[2] == candidate_value[3]:
                    true_tiles.update({(tile_key[0] + 1, tile_key[1]): [*flip_h(rot_270(candidate_value)), candidate_key]})
                elif tile_value[3] == candidate_value[0]:
                    true_tiles.update({(tile_key[0], tile_key[1] - 1): [*rot_270(candidate_value), candidate_key]})
                #off anti-clockwise with a twist
                elif tile_value[0] == candidate_value[1][::-1]:
                    true_tiles.update({(tile_key[0] - 1, tile_key[1]): [*rot_270(candidate_value), candidate_key]})
                elif tile_value[1] == candidate_value[2][::-1]:
                    true_tiles.update({(tile_key[0], tile_key[1] + 1): [*flip_v(rot_270(candidate_value)), candidate_key]})
                elif tile_value[2] == candidate_value[3][::-1]:
                    true_tiles.update({(tile_key[0] + 1, tile_key[1]): [*rot_270(candidate_value), candidate_key]})
                elif tile_value[3] == candidate_value[0][::-1]:
                    true_tiles.update({(tile_key[0], tile_key[1] - 1): [*flip_v(rot_270(candidate_value)), candidate_key]})
                else:
                    continue
                break
            else:
                continue
            tiles.pop(candidate_key)
            break
    return true_tiles

def construct_canvas(tiles):
    canvas = []
    for i in range(min_x, max_x + 1):
        for ii in range(0, 8):
            canvas.append('')
            for j in range(min_y, max_y + 1):
                canvas[-1] += tiles[(i, j)][4][ii]
    return canvas

def count_monsters(canvas):
    height = len(canvas)
    monsters = 0
    for i in range(0, height - 2):
        for j in range(0, height - 19):
            if canvas[i + 1][j + 0] == '#' \
            and canvas[i + 2][j + 1] == '#' \
            and canvas[i + 2][j + 4] == '#' \
            and canvas[i + 1][j + 5] == '#' \
            and canvas[i + 1][j + 6] == '#' \
            and canvas[i + 2][j + 7] == '#' \
            and canvas[i + 2][j + 10] == '#' \
            and canvas[i + 1][j + 11] == '#' \
            and canvas[i + 1][j + 12] == '#' \
            and canvas[i + 2][j + 13] == '#' \
            and canvas[i + 2][j + 16] == '#' \
            and canvas[i + 1][j + 17] == '#' \
            and canvas[i + 0][j + 18] == '#' \
            and canvas[i + 1][j + 18] == '#' \
            and canvas[i + 1][j + 19] == '#':
                monsters += 1
    return monsters





print('Test Data')

tiles = read_file('testinput.txt')
tiles = match_up(tiles)

min_x = min([t[0] for t in tiles])
max_x = max([t[0] for t in tiles])
min_y = min([t[1] for t in tiles])
max_y = max([t[1] for t in tiles])

print('Part One:')

print(tiles[(min_x, min_y)][5] * tiles[(min_x, max_y)][5] * tiles[(max_x, min_y)][5] * tiles[(max_x, max_y)][5])

print('Part Two:')

canvas = construct_canvas(tiles)
height = len(canvas)
pixel_count = sum([len([c for c in row if c == '#']) for row in canvas])
total_monsters = 0

total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)
canvas = [line[::-1] for line in canvas]
total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)

print(pixel_count - 15 * total_monsters)

print('Live Data')

tiles = read_file('input.txt')
tiles = match_up(tiles)

min_x = min([t[0] for t in tiles])
max_x = max([t[0] for t in tiles])
min_y = min([t[1] for t in tiles])
max_y = max([t[1] for t in tiles])

print('Part One:')

print(tiles[(min_x, min_y)][5] * tiles[(min_x, max_y)][5] * tiles[(max_x, min_y)][5] * tiles[(max_x, max_y)][5])

print('Part Two:')

canvas = construct_canvas(tiles)
height = len(canvas)
pixel_count = sum([len([c for c in row if c == '#']) for row in canvas])
total_monsters = 0

total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)
canvas = [line[::-1] for line in canvas]
total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)
canvas = [''.join([canvas[i][j] for i in range(0, height)]) for j in range(height - 1, -1, -1)]
total_monsters += count_monsters(canvas)

print(pixel_count - 15 * total_monsters)