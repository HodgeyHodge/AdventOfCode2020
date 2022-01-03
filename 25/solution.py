
def transform(subject_number, loop_size):
    out = 1
    for i in range(loop_size):
        out = (subject_number * out) % 20201227
    return out

def find_loop_size(public_key):
    out = 1
    for i in range(1, 20201227):
        out = (out * 7) % 20201227
        if out == public_key:
            return i

print('Test Data')

card_public_key = 5764801
door_public_key = 17807724

card_loop_size = find_loop_size(card_public_key)
door_loop_size = find_loop_size(door_public_key)

print(f'Found loop sizes {card_loop_size} and {door_loop_size}')

print(f'Encryption key: {transform(card_public_key, door_loop_size)}')
print(f'Encryption key: {transform(door_public_key, card_loop_size)}')
#print(f'Encryption key: {transform(7, card_loop_size * door_loop_size)}')

print('Live Data')

card_public_key = 15628416
door_public_key = 11161639

card_loop_size = find_loop_size(card_public_key)
door_loop_size = find_loop_size(door_public_key)

print(f'Found loop sizes {card_loop_size} and {door_loop_size}')

print(f'Encryption key: {transform(card_public_key, door_loop_size)}')
print(f'Encryption key: {transform(door_public_key, card_loop_size)}')


