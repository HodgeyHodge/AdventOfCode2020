
from queue import Queue
from functools import reduce

def move(decks):
    a = decks[0].get()
    b = decks[1].get()
    if a > b:
        decks[0].put(a)
        decks[0].put(b)
    else:
        decks[1].put(b)
        decks[1].put(a)

def play(decks, game_size):
    round = 0
    while not decks[0].empty() and not decks[1].empty():
        round += 1
        move(decks)
    if decks[0].empty():
        score = sum([a * b for a, b in zip(range(game_size, 0, -1), decks[1].queue)])
        print(f'Winner player {2}, on round {round}, score {score}')
    else:
        score = sum([a * b for a, b in zip(range(game_size, 0, -1), decks[0].queue)])
        print(f'Winner player {1}, on round {round}, score {score}')

print('Part One')

print('Test Data')

game_size = 10

decks = [
    Queue(maxsize = game_size),
    Queue(maxsize = game_size)
]

for card in [9, 2, 6, 3, 1]:
    decks[0].put(card)

for card in [5, 8, 4, 7, 10]:
    decks[1].put(card)
    
play(decks, game_size)

print('Live Data')

game_size = 50

decks = [
    Queue(maxsize = game_size),
    Queue(maxsize = game_size)
]

for card in [21, 50, 9, 45, 16, 47, 27, 38, 29, 48, 10, 42, 32, 31, 41, 11, 8, 33, 25, 30, 12, 40, 7, 23, 46]:
    decks[0].put(card)

for card in [22, 20, 44, 2, 26, 17, 34, 37, 43, 5, 15, 18, 36, 19, 24, 35, 3, 13, 14, 1, 6, 39, 49, 4, 28]:
    decks[1].put(card)

play(decks, game_size)

print('Part Two')













