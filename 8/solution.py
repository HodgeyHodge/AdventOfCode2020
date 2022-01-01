
def read_input(filename):
    with open(filename) as file:
        return [line.strip('\n') for line in file]

def run(instructions, i):
    used = []
    accumulator = 0
    current = 0
    while True:
        if current in used:
            return current, accumulator
        used.append(current)
        if current == len(instructions):
            return -1, accumulator
        instruction = instructions[current].split(' ')
        if instruction[0] == 'nop':
            if current == i:
                current += int(instruction[1])
            else:
                current += 1
        elif instruction[0] == 'acc':
            accumulator += int(instruction[1])
            current += 1
        elif instruction[0] == 'jmp':
            if current == i:
                current += 1
            else:
                current += int(instruction[1])

# part one

print(run(read_input('testinput.txt'), -1))
print(run(read_input('input.txt'), -1))

# part two

instructions = read_input('testinput.txt')
for i in range(0, len(instructions)):
    out = run(instructions, i)
    if out[0] == -1:
        print(out)

instructions = read_input('input.txt')
for i in range(0, len(instructions)):
    out = run(instructions, i)
    if out[0] == -1:
        print(out)
