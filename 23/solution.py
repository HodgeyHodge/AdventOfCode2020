
def descender(index, snip, length):
    descender = (index - 1) % length
    while True:
        if descender not in snip:
            return descender
        else:
            descender = (descender - 1) % length

def encode(circle):
    linked_list = [-1] * len(circle)
    for i in range(0, len(circle) - 1):
        linked_list[(0 if circle[i] == len(circle) else circle[i])] = (0 if circle[i + 1] == len(circle) else circle[i + 1])
    linked_list[(0 if circle[-1] == len(circle) else circle[-1])] = (0 if circle[0] == len(circle) else circle[0])
    return linked_list

def decode(linked_list):
    size = len(linked_list)
    i = 1
    out = ''
    for _ in range(0, len(linked_list) - 1):
        out = out + (str(size) if linked_list[i] == 0 else str(linked_list[i]))
        i = linked_list[i]
    return out

def play_v1(circle, active, rounds):
    linked_list = encode(circle)
    length = len(circle)
    for i in range(0, rounds):
        first = linked_list[active]
        second = linked_list[first]
        third = linked_list[second]
        fourth = linked_list[third]
        prev = descender(active, [first, second, third], length)
        next = linked_list[prev]
        linked_list[active] = fourth
        linked_list[prev] = first
        linked_list[third] = next
        active = fourth
    return decode(linked_list)
    
def play_v2(circle, active, rounds):
    linked_list = encode(circle)
    length = len(circle)
    for i in range(0, rounds):
        first = linked_list[active]
        second = linked_list[first]
        third = linked_list[second]
        fourth = linked_list[third]
        prev = descender(active, [first, second, third], length)
        next = linked_list[prev]
        linked_list[active] = fourth
        linked_list[prev] = first
        linked_list[third] = next
        active = fourth
    return linked_list[1] * linked_list[linked_list[1]]
    
print('Part One')

print('Test Data')
print(play_v1([3, 8, 9, 1, 2, 5, 4, 6, 7], 3, 10))
print(play_v2([3, 8, 9, 1, 2, 5, 4, 6, 7], 3, 10))
print(play_v1([3, 8, 9, 1, 2, 5, 4, 6, 7], 3, 100))
print(play_v2([3, 8, 9, 1, 2, 5, 4, 6, 7], 3, 100))

print('Live Data')
print(play_v1([4, 6, 3, 5, 2, 8, 1, 7, 9], 4, 100))
print(play_v2([4, 6, 3, 5, 2, 8, 1, 7, 9], 4, 100))

print('Part Two')

print('Test Data')
circle = [3, 8, 9, 1, 2, 5, 4, 6, 7] + [i for i in range(10, 1000001)]
print(play_v2(circle, 3, 10000000))

print('Live Data')
circle = [4, 6, 3, 5, 2, 8, 1, 7, 9] + [i for i in range(10, 1000001)]
print(play_v2(circle, 4, 10000000))
