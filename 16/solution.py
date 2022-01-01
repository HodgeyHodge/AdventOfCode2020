
from functools import reduce

def read_file(filename):
    with open(filename) as file:
        sections = file.read().split('\n\n')
    ranges = [range.split(': ') for range in sections[0].split('\n')]
    ranges = [[range[0]] + range[1].split(' or ') for range in ranges]
    ranges = dict([
        range[0], 
        [int(n) for n in range[1].split('-')] + [int(n) for n in range[2].split('-')]
    ] for range in ranges)
    my_ticket = tuple(int(n) for n in sections[1].split('\n')[1].split(','))
    tickets = [tuple(int(n) for n in row.split(',')) for row in sections[2].split('\n')[1:]]
    
    return ranges, my_ticket, tickets

def deduce(positions):
    for name in set(p[0] for p in positions):
        name_positions = [p for p in positions if p[0] == name]
        if len(name_positions) == 1:
            positions = name_positions + [p for p in positions if p[1] != name_positions[0][1]]
    for field in set(p[1] for p in positions):
        field_positions = [p for p in positions if p[1] == field]
        if len(field_positions) == 1:
            positions = field_positions + [p for p in positions if p[0] != field_positions[0][0]]
    return positions

print('Part one')

ranges, my_ticket, tickets = read_file('testinput.txt')

error_rate = 0
for t in tickets:
    for f in t:
        for r in ranges.values():
            if (f >= r[0] and f <= r[1]) or (f >= r[2] and f <= r[3]):
                break
        else:
            error_rate += f
print(error_rate)

ranges, my_ticket, tickets = read_file('input.txt')

error_rate = 0
for t in tickets:
    for f in t:
        for r in ranges.values():
            if (f >= r[0] and f <= r[1]) or (f >= r[2] and f <= r[3]):
                break
        else:
            error_rate += f
print(error_rate)

print('Part two')

ranges, my_ticket, tickets = read_file('input.txt')

valid_tickets = []
for t in tickets:
    for f in t:
        for r in ranges.values():
            if (f >= r[0] and f <= r[1]) or (f >= r[2] and f <= r[3]):
                break
        else:
            break
    else:
        valid_tickets.append(t)
        continue

valid_positions = []
for i in range(0, len(my_ticket)):
    for k, v in ranges.items():
        for t in valid_tickets:
            if (t[i] >= v[0] and t[i] <= v[1]) or (t[i] >= v[2] and t[i] <= v[3]):
                pass
            else:
                break
        else:
            valid_positions.append((k, i))

while True:
    prior_length = len(valid_positions)
    valid_positions = deduce(valid_positions)
    if len(valid_positions) == prior_length:
        break

print(reduce(lambda x, y: x * y, [my_ticket[v[1]] for v in valid_positions if v[0].startswith('departure ')]))














