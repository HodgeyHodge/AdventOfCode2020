
from math import ceil, floor

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
            if impure_key not in ['0', '8', '11']:
                for pure_key in pure_keys:
                    new_rule = [path for path in rules[impure_key] if pure_key not in path]
                    for impure_path in [path for path in rules[impure_key] if pure_key in path]:
                        for pure_path in rules[pure_key]:
                            new_path = impure_path[:]
                            new_path[new_path.index(pure_key):new_path.index(pure_key) + 1] = pure_path
                            new_rule.append(new_path)
                    rules[impure_key] = new_rule
        for pure_key in pure_keys:
            if pure_key != '0' and not any([path for k, v in rules.items() for path in v if pure_key in path]):
                rules.pop(pure_key)
        if len(impure_keys) <= 3:
            break

print('Test Data:')

rules, messages = read_file('testinput.txt')

reduce(rules)

print(rules)

rule_42 = [''.join(path) for path in rules['42']]
rule_31 = [''.join(path) for path in rules['31']]

print(f'Rule 42: {rule_42}')
print(f'Rule 31: {rule_31}')

valid = 0
for message in messages:
    for i in range(ceil((len(message)//5 + 1) / 2), len(message)//5):
        for j in range(0, len(message)//5):
            if j < i:
                if message[5 * j:5 * j + 5] in rule_42:
                    pass
                else:
                    break
            else:
                if message[5 * j:5 * j + 5] in rule_31:
                    pass
                else:
                    break
        else:
            valid += 1
            break

print(valid)


print('Live Data:')

rules, messages = read_file('input.txt')

reduce(rules)

print(rules)

rule_42 = [''.join(path) for path in rules['42']]
rule_31 = [''.join(path) for path in rules['31']]

print(f'Rule 42: {rule_42}')
print(f'Rule 31: {rule_31}')

valid = 0
for message in messages:
    for i in range(ceil((len(message)//8 + 1) / 2), len(message)//8):
        for j in range(0, len(message)//8):
            if j < i:
                if message[8 * j:8 * j + 8] in rule_42:
                    pass
                else:
                    break
            else:
                if message[8 * j:8 * j + 8] in rule_31:
                    pass
                else:
                    break
        else:
            valid += 1
            break

print(valid)















