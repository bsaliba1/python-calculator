import tokenizer

EXIT = "exit"

# Evaluate input
def evaluate_input(line):
    if line == EXIT:
        quit(1)
    tokenizer.tokenize_line(line)

# Take in a line of input from std_in
def get_input():
    return input("> ")

# Take in input and evalutate the input
def driver():
    while True:
        line = get_input()
        evaluation = evaluate_input(line)

driver()
