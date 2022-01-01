
def read_input(filename):
    with open(filename) as file:
        return [line.strip('\n') for line in file]

COMPASS = 'NESW'

def turn(position, direction, degrees):
    return COMPASS[(COMPASS.find(position) + (-1 if direction == 'L' else 1) * int(degrees / 90)) % 4]

def turn_waypoint(waypoint_coords, direction, degrees):
    if direction == 'R':
        if degrees == 90:
            return [-waypoint_coords[1], waypoint_coords[0]]
        elif degrees == 180:
            return [-waypoint_coords[0], -waypoint_coords[1]]
        elif degrees == 270:
            return [waypoint_coords[1], -waypoint_coords[0]]
    elif direction == 'L':
        if degrees == 90:
            return [waypoint_coords[1], -waypoint_coords[0]]
        elif degrees == 180:
            return [-waypoint_coords[0], -waypoint_coords[1]]
        elif degrees == 270:
            return [-waypoint_coords[1], waypoint_coords[0]]

def follow_instruction(coords, direction, instruction):
    if instruction[0] == 'N':
        coords[0] += int(instruction[1:])
    elif instruction[0] == 'E':
        coords[1] += int(instruction[1:])
    elif instruction[0] == 'S':
        coords[0] -= int(instruction[1:])
    elif instruction[0] == 'W':
        coords[1] -= int(instruction[1:])
    elif instruction[0] == 'L':
        direction = turn(direction, 'L', int(instruction[1:]))
    elif instruction[0] == 'R':
        direction = turn(direction, 'R', int(instruction[1:]))
    elif instruction[0] == 'F':
        coords, direction = follow_instruction(coords, direction, direction + instruction[1:])
    return coords, direction

def follow_waypoint_instruction(coords, waypoint_coords, instruction):
    if instruction[0] == 'N':
        waypoint_coords[0] += int(instruction[1:])
    elif instruction[0] == 'E':
        waypoint_coords[1] += int(instruction[1:])
    elif instruction[0] == 'S':
        waypoint_coords[0] -= int(instruction[1:])
    elif instruction[0] == 'W':
        waypoint_coords[1] -= int(instruction[1:])
    elif instruction[0] == 'L':
        waypoint_coords = turn_waypoint(waypoint_coords, 'L', int(instruction[1:]))
    elif instruction[0] == 'R':
        waypoint_coords = turn_waypoint(waypoint_coords, 'R', int(instruction[1:]))
    elif instruction[0] == 'F':
        coords[0] = coords[0] + waypoint_coords[0] * int(instruction[1:])
        coords[1] = coords[1] + waypoint_coords[1] * int(instruction[1:])
    return coords, waypoint_coords

instructions = read_input('testinput.txt')
coords = [0, 0]
direction = 'E'
for instruction in instructions:
    coords, direction = follow_instruction(coords, direction, instruction)
print(abs(coords[0]) + abs(coords[1]))

instructions = read_input('input.txt')
coords = [0, 0]
direction = 'E'
for instruction in instructions:
    coords, direction = follow_instruction(coords, direction, instruction)
print(abs(coords[0]) + abs(coords[1]))

instructions = read_input('testinput.txt')
coords = [0, 0]
waypoint_coords = [1, 10]
for instruction in instructions:
    coords, waypoint_coords = follow_waypoint_instruction(coords, waypoint_coords, instruction)
print(abs(coords[0]) + abs(coords[1]))

instructions = read_input('input.txt')
coords = [0, 0]
waypoint_coords = [1, 10]
for instruction in instructions:
    coords, waypoint_coords = follow_waypoint_instruction(coords, waypoint_coords, instruction)
print(abs(coords[0]) + abs(coords[1]))









