
from functools import reduce

def read_file(filename):
    with open(filename) as file:
        return [[symbol for symbol in line.strip('\n').replace('(', '( ').replace(')', ' )').split(' ')] for line in file]

def unbracket(expression):
    opener = None
    for position, symbol in enumerate(expression):
        if symbol == '(':
            opener = position
        if symbol == ')':
            subexpression = expression[opener+1:position]
            return expression[:opener] + [evaluate(subexpression)] + expression[position+1:]

def unbracket_with_precedence(expression):
    opener = None
    for position, symbol in enumerate(expression):
        if symbol == '(':
            opener = position
        if symbol == ')':
            subexpression = expression[opener+1:position]
            return expression[:opener] + [evaluate_with_precedence(subexpression)] + expression[position+1:]

def perform_addition(expression):
    print(f'rebracketing this shit:')
    print(expression)
    for position, symbol in enumerate(expression):
        if symbol == '+' and expression[position - 1] not in ['(', ')'] and expression[position + 1] not in ['(', ')']:
            return expression[:(position - 1)] + \
            [str(int(expression[position - 1]) + int(expression[position + 1]))] + \
            expression[(position + 2):]

def evaluate(expression):
    while '(' in expression:
        expression = unbracket(expression)
    running_total = 0
    current_operation = '+'
    for position, symbol in enumerate(expression):
        if symbol in ['+', '*']:
            current_operation = symbol
        else:
            if current_operation == '+':
                running_total += int(symbol)
            else:
                running_total *= int(symbol)
    return running_total

def evaluate_with_precedence(expression):
    while '(' in expression:
        expression = unbracket_with_precedence(expression)
    
    while '+' in expression:
        expression = perform_addition(expression)
    
    return reduce(lambda x, y: x * y, [int(x) for x in expression if x != '*'])





assert(evaluate(list('1+2*3+4*5+6')) == 71)
assert(evaluate(list('1+(2*3)+(4*(5+6))')) == 51)
assert(evaluate(list('2*3+(4*5)')) == 26)
assert(evaluate(list('5+(8*3+9+3*4*3)')) == 437)
assert(evaluate(list('5*9*(7*3*3+9*3+(8+6*4))')) == 12240)
assert(evaluate(list('((2+4*9)*(6+9*8+6)+6)+2+4*2')) == 13632)

assert(evaluate_with_precedence(list('1+2*3+4*5+6')) == 231)
assert(evaluate_with_precedence(list('1+(2*3)+(4*(5+6))')) == 51)
assert(evaluate_with_precedence(list('2*3+(4*5)')) == 46)
assert(evaluate_with_precedence(list('5+(8*3+9+3*4*3)')) == 1445)
assert(evaluate_with_precedence(list('5*9*(7*3*3+9*3+(8+6*4))')) == 669060)
assert(evaluate_with_precedence(list('((2+4*9)*(6+9*8+6)+6)+2+4*2')) == 23340)





expressions = read_file('input.txt')
total = 0
for e in expressions:
    total += evaluate(e)
print(total)

expressions = read_file('input.txt')
total = 0
for e in expressions:
    total += evaluate_with_precedence(e)
print(total)
