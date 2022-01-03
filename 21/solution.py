
def read_file(filename):
    with open(filename) as file:
        lines = [line.split(' (contains ') for line in file.readlines()]
    return [(line[0].split(' '), line[1].strip(')\n').split(', ')) for line in lines]

def reduce_allergen_locations(file):
    ingredients = set().union(*[line[0] for line in file])
    allergens = set().union(*[line[1] for line in file])
    locations = {}
    
    for allergen in allergens:
        candidate_ingredients = ingredients.copy()
        for line in file:
            if allergen in line[1]:
                candidate_ingredients = candidate_ingredients.intersection(line[0])
        locations[allergen] = list(candidate_ingredients)
    return locations

def deduce_allergen_locations(locations):
    determined = {}
    while True:
        for k, v in locations.items():
            if len(v) == 1:
                determined[k] = v
                for k_, v_ in locations.items():
                    locations[k_] = [word for word in v_ if word != v[0]]
                break
        if max([len(v) for k, v in locations.items()]) == 0:
            break
    return determined

print('Test Data')
print('Part One')

file = read_file('testinput.txt')
locations = reduce_allergen_locations(file)
safe_words = set().union(*[line[0] for line in file]).difference(*[v for v in locations.values()])
print(sum([len([word for word in line[0] if word in safe_words]) for line in file]))

print('Part Two')

locations = deduce_allergen_locations(locations)
print(','.join([locations[k][0] for k in sorted(locations)]))

print('Live Data')
print('Part One')

file = read_file('input.txt')
locations = reduce_allergen_locations(file)
safe_words = set().union(*[line[0] for line in file]).difference(*[v for v in locations.values()])
print(sum([len([word for word in line[0] if word in safe_words]) for line in file]))

print('Part Two')

locations = deduce_allergen_locations(locations)
print(','.join([locations[k][0] for k in sorted(locations)]))









