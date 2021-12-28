
def load_file(filename):
    nodes = set()
    edges = set()
    with open(filename) as file:
        for line in file:
            line = line.split(' bags contain ')
            nodes.add(line[0])
            next = line[1].strip('\n').split(', ')
            for bag in next:
                bag = bag.split(' ')
                if bag[0] != 'no':
                    edges.add((line[0], bag[1] + ' ' + bag[2], int(bag[0])))
    return nodes, edges
    
def bags_inside(edges, bag):
    contents = [edge for edge in edges if edge[0] == bag]
    if len(contents) == 0:
        return 0
    else:
        return sum([c[2] * (1 + bags_inside(edges, c[1])) for c in contents])





def part_one(filename):
    nodes, edges = load_file(filename)
    wins = 0

    for n in nodes:
        bags = [n]
        while True:
            bags = [next[1] for next in edges if next[0] in bags]
            if 'shiny gold' in bags:
                wins += 1
                break
            if len(bags) == 0:
                break
    return wins

def part_two(filename):
    nodes, edges = load_file(filename)
    return bags_inside(edges, 'shiny gold')





print(part_one('testinput1.txt'))
print(part_one('input.txt'))

print(part_two('testinput1.txt'))
print(part_two('testinput2.txt'))
print(part_two('input.txt'))

