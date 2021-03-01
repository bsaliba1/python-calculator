import tokenizer
from evaluator import Evaluator

EXIT = "exit"

# Evaluate input
def evaluate_input(line):
    if line == EXIT:
        quit(1)
    tokens = tokenizer.tokenize_line(line)
    evaluator = Evaluator(tokens)
    result = evaluator.expr()
    print(result)

# Take in a line of input from std_in
def get_input():
    return input("calc> ")

# Take in input and evalutate the input
def driver():
    while True:
        line = get_input()
        evaluation = evaluate_input(line)

driver()
