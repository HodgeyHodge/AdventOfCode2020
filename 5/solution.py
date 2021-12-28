
def get_seat(code):
    return 64 * (code[0] == 'B') + \
           32 * (code[1] == 'B') + \
           16 * (code[2] == 'B') + \
           8 * (code[3] == 'B') + \
           4 * (code[4] == 'B') + \
           2 * (code[5] == 'B') + \
           1 * (code[6] == 'B'), \
           4 * (code[7] == 'R') + \
           2 * (code[8] == 'R') + \
           1 * (code[9] == 'R')

with open('input.txt') as file:
    f = [c for c in file.readlines()]

ids = [8 * get_seat(c)[0] + get_seat(c)[1] for c in f]

print(max(ids))

for i in range(0, max(ids)):
    if i not in ids and i + 1 in ids and i - 1 in ids:
        print(i)
