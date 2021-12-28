from functools import reduce

with open('input.txt') as file:
    f = [l.split('\n') for l in file.read().split('\n\n')]

print(sum([len(set(char for string in group for char in string)) for group in f]))

print(sum([len(reduce(lambda s, t: s.intersection(t), [set(string) for string in group])) for group in f]))
