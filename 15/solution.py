
def play(prev_spoken, last_spoken, turns):
    i = len(prev_spoken) + 1
    while True:
        if last_spoken in prev_spoken:
            diff = i - prev_spoken[last_spoken]
            prev_spoken[last_spoken] = i
            last_spoken = diff
        else:
            prev_spoken[last_spoken] = i
            last_spoken = 0
        i += 1
        if i == turns:
            return last_spoken

print('Part one: test data')

prev_spoken = {
    0: 1,
    3: 2
}

last_spoken = 6

print(play(prev_spoken, last_spoken, 2020))

print('Part one: live data')

prev_spoken = {
    2: 1,
    0: 2,
    1: 3,
    7: 4,
    4: 5,
    14: 6
}

last_spoken = 18

print(play(prev_spoken, last_spoken, 2020))

prev_spoken = {
    2: 1,
    0: 2,
    1: 3,
    7: 4,
    4: 5,
    14: 6
}

last_spoken = 18

print(play(prev_spoken, last_spoken, 30000000))

