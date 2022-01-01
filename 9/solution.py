
def read_input(filename):
    with open(filename) as file:
        return [int(line.strip('\n')) for line in file]
        
def part_one(input, preamble_length):
    for i in range(preamble_length, len(input)):
        ok = False
        for j in range(i - 1, i - preamble_length - 1, -1):
            for k in range(i - 1, i - preamble_length - 1, -1):
                if input[j] + input[k] == input[i]:
                    ok = True
        if not ok:
            print(input[i])

def part_two(input, magic_number):
    for i in range(0, len(input)):
        total = 0
        j = 0
        while total < magic_number:
            total += input[i + j]
            if total == magic_number:
                print(min(input[i:i+j+1]) + max(input[i:i+j+1]))
                break
            j += 1
        else:
            continue
        break

part_one(read_input('testinput.txt'), 5)
part_one(read_input('input.txt'), 25)

part_two(read_input('testinput.txt'), 127)
part_two(read_input('input.txt'), 393911906)
