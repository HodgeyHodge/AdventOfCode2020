
def read_input(filename):
    with open(filename) as file:
        return [row.strip('\n') for row in file.readlines()]

def apply_mask_to_decimal_integer(mask, integer):
    bin_string = format(integer, 'b').zfill(36)
    bits = [bin_string[i] if mask[i] == 'X' else mask[i] for i in range(0, 36)]
    return int(''.join(bits), 2)

def apply_floaty_mask_to_decimal_integer(mask, integer):
    bin_string = format(integer, 'b').zfill(36)
    output = ['']
    for i in range(0, 36):
        if mask[i] == '0':
            output = [s + bin_string[i] for s in output]
        elif mask[i] == '1':
            output = [s + '1' for s in output]
        elif mask[i] == 'X':
            output = [s + '1' for s in output] + [s + '0' for s in output]
    return output

print('Part one:')

instructions = read_input('input.txt')
mem = {}
mask = ''

for instruction in instructions:
    if instruction.startswith('mask = '):
        mask = instruction.split(' = ')[1]
    if instruction.startswith('mem['):
        address = instruction.replace('mem[', '').split('] = ')[0]
        value = int(instruction.replace('mem[', '').split('] = ')[1])
        mem[address] = apply_mask_to_decimal_integer(mask, value)

print(sum([v for v in mem.values()]))

print('Part two:')

instructions = read_input('input.txt')
mem = {}
mask = ''

for instruction in instructions:
    if instruction.startswith('mask = '):
        mask = instruction.split(' = ')[1]
    if instruction.startswith('mem['):
        address = int(instruction.replace('mem[', '').split('] = ')[0])
        value = int(instruction.replace('mem[', '').split('] = ')[1])
        for a in apply_floaty_mask_to_decimal_integer(mask, address):
            mem[a] = value
        
print(sum([v for v in mem.values()]))
