import requests
import operator

def hello_world():
    return "Hello world !"

def add_element(first, second):
    op = get_operator(second)
    operande = int(second[1:])
    return op(first, operande)

def get_operator(input):
    op = input[:1]
    if op == '+':
        return operator.add
    return operator.sub

def reduce_input(input):
    return reduce(add_element, input, 0)
    
def get_code():
    with open('input') as f:
        input = f.readlines()
    f.closed
    val = map(lambda s: s.replace('\n', ''), input)
    conc = reduce_input(val)
    print(conc)


get_code()