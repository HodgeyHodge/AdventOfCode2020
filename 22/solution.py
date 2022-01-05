
from queue import Queue

def create_decks(deck_one, deck_two):
    decks = [Queue(), Queue()]
    for card in deck_one:
        decks[0].put(card)
    for card in deck_two:
        decks[1].put(card)
    return decks

def move(decks):
    a = decks[0].get()
    b = decks[1].get()
    if a > b:
        decks[0].put(a)
        decks[0].put(b)
    else:
        decks[1].put(b)
        decks[1].put(a)

def play_v1(decks):
    round = 0
    while not decks[0].empty() and not decks[1].empty():
        round += 1
        move(decks)
    if decks[0].empty():
        return 2, round, decks[1]
    else:
        return 2, round, decks[0]

def play_v2(decks):
    round = 0
    deck_history = {}
    while True:
        if decks[0].empty():
            return 1, round, decks[1]
        elif decks[1].empty():
            return 0, round, decks[0]
        if any([v for v in deck_history.values() if v[0] == list(decks[0].queue) and v[1] == list(decks[1].queue)]):
            return 0, round, decks[0]
        round += 1
        deck_history[round] = (list(decks[0].queue), list(decks[1].queue))
        a = decks[0].get()
        b = decks[1].get()
        if a <= decks[0].qsize() and b <= decks[1].qsize():
            new_decks = [Queue(), Queue()]
            for i in range(0, a):
                new_decks[0].put(list(decks[0].queue)[i])
            for i in range(0, b):
                new_decks[1].put(list(decks[1].queue)[i])
            winner, _, _ = play_v2(new_decks)
            if winner == 0:
                decks[0].put(a)
                decks[0].put(b)
            elif winner == 1:
                decks[1].put(b)
                decks[1].put(a)
        else:
            if a > b:
                decks[0].put(a)
                decks[0].put(b)
            else:
                decks[1].put(b)
                decks[1].put(a)

print('Test Data:')
print('Part One:')

decks = create_decks(
    [9, 2, 6, 3, 1],
    [5, 8, 4, 7, 10]
)

winner, round, winning_deck = play_v1(decks)
score = sum([a * b for a, b in zip(range(winning_deck.qsize(), 0, -1), winning_deck.queue)])
print(f'Winner player {winner} on round {round}, score: {score}')

print('Part Two:')

decks = create_decks(
    [9, 2, 6, 3, 1],
    [5, 8, 4, 7, 10]
)

winner, round, winning_deck = play_v2(decks)
score = sum([a * b for a, b in zip(range(winning_deck.qsize(), 0, -1), winning_deck.queue)])
print(f'Winner player {winner} on round {round}, score: {score}')

print('Live Data:')
print('Part One:')

decks = create_decks(
    [21, 50, 9, 45, 16, 47, 27, 38, 29, 48, 10, 42, 32, 31, 41, 11, 8, 33, 25, 30, 12, 40, 7, 23, 46],
    [22, 20, 44, 2, 26, 17, 34, 37, 43, 5, 15, 18, 36, 19, 24, 35, 3, 13, 14, 1, 6, 39, 49, 4, 28]
)

winner, round, winning_deck = play_v1(decks)
score = sum([a * b for a, b in zip(range(winning_deck.qsize(), 0, -1), winning_deck.queue)])
print(f'Winner player {winner} on round {round}, score: {score}')

print('Part Two:')

decks = create_decks(
    [21, 50, 9, 45, 16, 47, 27, 38, 29, 48, 10, 42, 32, 31, 41, 11, 8, 33, 25, 30, 12, 40, 7, 23, 46],
    [22, 20, 44, 2, 26, 17, 34, 37, 43, 5, 15, 18, 36, 19, 24, 35, 3, 13, 14, 1, 6, 39, 49, 4, 28]
)
    
winner, round, winning_deck = play_v2(decks)
score = sum([a * b for a, b in zip(range(winning_deck.qsize(), 0, -1), winning_deck.queue)])
print(f'Winner player {winner} on round {round}, score: {score}')
