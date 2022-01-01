
def move(circle):
    current = circle[0]
    snip = circle[1:4]
    next = (current - 1) % 9 if (current - 1) % 9 not in snip else ((current - 2) % 9 if (current - 2) % 9 not in snip else ((current - 3) % 9 if (current - 3) % 9 not in snip else (current - 4) % 9))
    circle = circle[4:] + [circle[0]]
    index = circle.index(next)
    circle = circle[:index + 1] + snip + circle[index + 1:]
    return circle

print('Part One')

print('Test Data')

circle = [3, 8, 0, 1, 2, 5, 4, 6, 7]

for i in range(0, 100):
    circle = move(circle)

print(circle)

print('Live Data')

circle = [4, 6, 3, 5, 2, 8, 1, 7, 0]

for i in range(0, 100):
    circle = move(circle)

print(circle)

print('Part Two')

