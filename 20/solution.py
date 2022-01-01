
def read_file(filename):
    with open(filename) as file:
        dict = {}
        tile_content = []
        for line in file:
            if line.startswith('Tile '):
                current_tile = int(line.replace('Tile ', '').replace(':\n', ''))
            elif len(line) == 1:
                dict[current_tile] = tile_content
                tile_content = []
            else:
                tile_content.append(line.strip('\n'))
        dict[current_tile] = tile_content
    return dict

def get_edge(tile, side, direction):
    edge = ''
    if side == 'N':
        edge = tile[0]
    elif side == 'E':
        edge = ''.join([tile[i][9] for i in range(0, 10)])
    elif side == 'S':
        edge = tile[9]
    elif side == 'W':
        edge = ''.join([tile[i][0] for i in range(0, 10)])
    return edge[::-1] if direction == -1 else edge

def get_matches(tiles):
    matches = []
    for tile in tiles:
        for potential_match in [t for t in tiles if t > tile]:
            if get_edge(tiles[tile], 'N', 1) == get_edge(tiles[potential_match], 'N', 1):
                matches.append((tile, potential_match, 'N', 1, 'N', 1))
            if get_edge(tiles[tile], 'N', 1) == get_edge(tiles[potential_match], 'N', -1):
                matches.append((tile, potential_match, 'N', 1, 'N', -1))
            if get_edge(tiles[tile], 'N', 1) == get_edge(tiles[potential_match], 'E', 1):
                matches.append((tile, potential_match, 'N', 1, 'E', 1))
            if get_edge(tiles[tile], 'N', 1) == get_edge(tiles[potential_match], 'E', -1):
                matches.append((tile, potential_match, 'N', 1, 'E', -1))
            if get_edge(tiles[tile], 'N', 1) == get_edge(tiles[potential_match], 'S', 1):
                matches.append((tile, potential_match, 'N', 1, 'S', 1))
            if get_edge(tiles[tile], 'N', 1) == get_edge(tiles[potential_match], 'S', -1):
                matches.append((tile, potential_match, 'N', 1, 'S', -1))
            if get_edge(tiles[tile], 'N', 1) == get_edge(tiles[potential_match], 'W', 1):
                matches.append((tile, potential_match, 'N', 1, 'W', 1))
            if get_edge(tiles[tile], 'N', 1) == get_edge(tiles[potential_match], 'W', -1):
                matches.append((tile, potential_match, 'N', 1, 'W', -1))
            if get_edge(tiles[tile], 'E', 1) == get_edge(tiles[potential_match], 'N', 1):
                matches.append((tile, potential_match, 'E', 1, 'N', 1))
            if get_edge(tiles[tile], 'E', 1) == get_edge(tiles[potential_match], 'N', -1):
                matches.append((tile, potential_match, 'E', 1, 'N', -1))
            if get_edge(tiles[tile], 'E', 1) == get_edge(tiles[potential_match], 'E', 1):
                matches.append((tile, potential_match, 'E', 1, 'E', 1))
            if get_edge(tiles[tile], 'E', 1) == get_edge(tiles[potential_match], 'E', -1):
                matches.append((tile, potential_match, 'E', 1, 'E', -1))
            if get_edge(tiles[tile], 'E', 1) == get_edge(tiles[potential_match], 'S', 1):
                matches.append((tile, potential_match, 'E', 1, 'S', 1))
            if get_edge(tiles[tile], 'E', 1) == get_edge(tiles[potential_match], 'S', -1):
                matches.append((tile, potential_match, 'E', 1, 'S', -1))
            if get_edge(tiles[tile], 'E', 1) == get_edge(tiles[potential_match], 'W', 1):
                matches.append((tile, potential_match, 'E', 1, 'W', 1))
            if get_edge(tiles[tile], 'E', 1) == get_edge(tiles[potential_match], 'W', -1):
                matches.append((tile, potential_match, 'E', 1, 'W', -1))
            if get_edge(tiles[tile], 'S', 1) == get_edge(tiles[potential_match], 'N', 1):
                matches.append((tile, potential_match, 'S', 1, 'N', 1))
            if get_edge(tiles[tile], 'S', 1) == get_edge(tiles[potential_match], 'N', -1):
                matches.append((tile, potential_match, 'S', 1, 'N', -1))
            if get_edge(tiles[tile], 'S', 1) == get_edge(tiles[potential_match], 'E', 1):
                matches.append((tile, potential_match, 'S', 1, 'E', 1))
            if get_edge(tiles[tile], 'S', 1) == get_edge(tiles[potential_match], 'E', -1):
                matches.append((tile, potential_match, 'S', 1, 'E', -1))
            if get_edge(tiles[tile], 'S', 1) == get_edge(tiles[potential_match], 'S', 1):
                matches.append((tile, potential_match, 'S', 1, 'S', 1))
            if get_edge(tiles[tile], 'S', 1) == get_edge(tiles[potential_match], 'S', -1):
                matches.append((tile, potential_match, 'S', 1, 'S', -1))
            if get_edge(tiles[tile], 'S', 1) == get_edge(tiles[potential_match], 'W', 1):
                matches.append((tile, potential_match, 'S', 1, 'W', 1))
            if get_edge(tiles[tile], 'S', 1) == get_edge(tiles[potential_match], 'W', -1):
                matches.append((tile, potential_match, 'S', 1, 'W', -1))
            if get_edge(tiles[tile], 'W', 1) == get_edge(tiles[potential_match], 'N', 1):
                matches.append((tile, potential_match, 'W', 1, 'N', 1))
            if get_edge(tiles[tile], 'W', 1) == get_edge(tiles[potential_match], 'N', -1):
                matches.append((tile, potential_match, 'W', 1, 'N', -1))
            if get_edge(tiles[tile], 'W', 1) == get_edge(tiles[potential_match], 'E', 1):
                matches.append((tile, potential_match, 'W', 1, 'E', 1))
            if get_edge(tiles[tile], 'W', 1) == get_edge(tiles[potential_match], 'E', -1):
                matches.append((tile, potential_match, 'W', 1, 'E', -1))
            if get_edge(tiles[tile], 'W', 1) == get_edge(tiles[potential_match], 'S', 1):
                matches.append((tile, potential_match, 'W', 1, 'S', 1))
            if get_edge(tiles[tile], 'W', 1) == get_edge(tiles[potential_match], 'S', -1):
                matches.append((tile, potential_match, 'W', 1, 'S', -1))
            if get_edge(tiles[tile], 'W', 1) == get_edge(tiles[potential_match], 'W', 1):
                matches.append((tile, potential_match, 'W', 1, 'W', 1))
            if get_edge(tiles[tile], 'W', 1) == get_edge(tiles[potential_match], 'W', -1):
                matches.append((tile, potential_match, 'W', 1, 'W', -1))
    return matches
    

tiles = read_file('input.txt')
matches = get_matches(tiles)

print('Part one:')

num_connections = [(tile, len([match for match in matches if (match[0] == tile or match[1] == tile)])) for tile in tiles]

for connection in num_connections:
    if connection[1] == 2:
        print(connection)

print('Part two:')

print(matches)





