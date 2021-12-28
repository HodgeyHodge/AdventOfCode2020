with open('input.txt') as file:
    s = [l.strip('\n') for l in file.readlines()]

for k in [1, 3, 5, 7]:
    trees = 0
    i = 0
    for l in s:
        trees += (l[i] == '#')
        i = (i + k) % len(l)
    print(trees)

trees = 0
i = 0
skip = False
for l in s:
    if not skip:
        trees += (l[i] == '#')
        i = (i + 1) % len(l)
    skip = not skip
print(trees)


