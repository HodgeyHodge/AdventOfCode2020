
def read_file(filename):
    with open(filename) as file:
        rules, messages = file.read().split('\n\n')
        rules = dict([rule.replace('"', '').split(': ') for rule in rules.split('\n')])
        for rule in rules:
            rules[rule] = [[n for n in part.split(' ')] for part in rules[rule].split(' | ')]
        messages = messages.split('\n')
        return rules, messages

def contains_numerals(path):
    return any(c.isdigit() for c in path)

def reduce(rules):
    while True:
        pure_keys = [rule for rule in rules if not any(contains_numerals(path) for path in rules[rule])]
        impure_keys = [rule for rule in rules if any(contains_numerals(path) for path in rules[rule])]
        for impure_key in impure_keys:
            for pure_key in pure_keys:
                new_rule = [path for path in rules[impure_key] if pure_key not in path]
                for impure_path in [path for path in rules[impure_key] if pure_key in path]:
                    for pure_path in rules[pure_key]:
                        new_path = impure_path[:]
                        new_path[new_path.index(pure_key):new_path.index(pure_key) + 1] = pure_path
                        new_rule.append(new_path)
                rules[impure_key] = new_rule
        if len(impure_keys) == 0:
            break

print('Test Data:')

rules, messages = read_file('testinput.txt')

reduce(rules)

rules_out = set([''.join(path) for path in rules['0']])
valid = rules_out & set(messages)

print(len(valid))

print('Live Data:')

rules, messages = read_file('input.txt')

reduce(rules)

rules_out = set([''.join(path) for path in rules['0']])
valid = rules_out & set(messages)

print(len(valid))




