
def read_input(filename):
    with open(filename) as file:
        return [int(line.strip('\n')) for line in file]

def count_gaps(f):
    a = sum([(1 if f[j+1] == f[j] + 1 else 0) for j in range(0, len(f) - 1)])
    b = sum([(1 if f[j+1] == f[j] + 3 else 0) for j in range(0, len(f) - 3)])
    return (a + 1) * (b + 1)

def count_solutions(f):
    g = [0] * len(f)
    for i in range(len(f) - 1, -1, -1):
        if i == len(f) - 1:
            g[i] = 1
        else:
            g[i] = (g[i + 1] if (i + 1 < len(f) and f[i + 1] <= f[i] + 3) else 0) + \
                (g[i + 2] if (i + 2 < len(f) and f[i + 2] <= f[i] + 3) else 0) + \
                (g[i + 3] if (i + 3 < len(f) and f[i + 3] <= f[i] + 3) else 0)
    return g[0]
    

# part one

f = read_input('testinput.txt')
f.sort()
print(count_gaps(f))

f = read_input('input.txt')
f.sort()
print(count_gaps(f))

# part two

f = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
print(count_solutions(f))

f = read_input('testinput.txt')
f.sort()
f = [0] + f
print(count_solutions(f))

f = read_input('input.txt')
f.sort()
f = [0] + f
print(count_solutions(f))

