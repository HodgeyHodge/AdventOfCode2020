with open('input.txt') as file:
    f = [[x for x in l.strip('\n').split(' ')] for l in file.readlines()]

valid = 0
for l in f:
    if l[2].count(l[1][0]) >= int(l[0].split('-')[0]) and l[2].count(l[1][0]) <= int(l[0].split('-')[1]):
        valid += 1
print(valid)

valid = 0
for l in f:
    if (l[2][int(l[0].split('-')[0]) - 1] == l[1][0]) != (l[2][int(l[0].split('-')[1]) - 1] == l[1][0]):
        valid += 1
print(valid)
