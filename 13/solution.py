
from functools import reduce

def extended_euclid(n, N): 
    if n == 0:
        return 0, 1
    x, y = extended_euclid(N % n, n)
    m = y - (N // n) * x
    M = x
    return int(m), int(M)

print('Part one, test data:')

t = 939
busses = [7,13,59,31,19]

wait = t
for bus in busses:
    if bus - t % bus < wait:
        wait = bus - t % bus
        print(f'Faster bus found: {bus}, waiting time: {wait}, answer code: {bus * wait}')

print('Part one, live data:')

t = 1002561
busses = [1737,409,29,13,23,373,41,19]

wait = t
for bus in busses:
    if bus - t % bus < wait:
        wait = bus - t % bus
        print(f'Faster bus found: {bus}, waiting time: {wait}, answer code: {bus * wait}')

print('Part two, test data:')

input = [
    (7, 0),
    (13, 1),
    (59, 4),
    (31, 6),
    (19, 7)
]

busses = [line[0] for line in input]

N = reduce(lambda x, y: x * y, busses)

remainders = [line[0] - line[1] for line in input]

bezout_numbers = [extended_euclid(bus, N / bus) for bus in busses]

x = sum([remainders[i] * bezout_numbers[i][1] * N // busses[i] for i in range(0, len(input))])

while x < 0:
    x += N

print(x)

print('Part two, live data:')

input = [
    (17, 0),
    (37, 11),
    (409, 17),
    (29, 19),
    (13, 30),
    (23, 40),
    (373, 48),
    (41, 58),
    (19, 67)
]

busses = [line[0] for line in input]
N = reduce(lambda x, y: x * y, busses)
remainders = [line[0] - line[1] for line in input]
bezout_numbers = [extended_euclid(bus, N / bus) for bus in busses]

print(busses, N, remainders, bezout_numbers)

x = sum([remainders[i] * bezout_numbers[i][1] * N // busses[i] for i in range(0, len(input))])

while x < 0:
    x += N

print(x)
