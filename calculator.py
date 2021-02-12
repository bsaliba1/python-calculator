import re

EXIT = "exit"
AVAILABLE_TOKENS = {
        "NUMBER": "\d+",
        "ADDITION": "\+",
        }
ALL_TOKENS = {
        **AVAILABLE_TOKENS,

        # Variables
        "VARIABLE_NAME": "_*\w+_*",

        # Data Types
        "STRING": "\".*\"|'.*'",

        # Assignments
        "ASSIGNMENT": "=",

        # Arithmetic Operators
        "SUBTRACTION": "-",
        "MULTIPLICATION": "*",
        "DIVISION": "/",

        # Conditionals
        "IF": "if",
        "ELSE": "else",
        "WHILE": "while",

        # Boolean Operators
        "DOUBLE_EQUAL": "==",
        }

ALL_AVAILABLE_TOKENS_REGEXES = list(AVAILABLE_TOKENS.values())
UNAVAILABLE_TOKENS_REGEX = "[^"+("".join(ALL_AVAILABLE_TOKENS_REGEXES))+"]"
AVAILABLE_TOKENS_REGEX = "|".join(ALL_AVAILABLE_TOKENS_REGEXES)

# Return an invalid token if one exists in the line otherwise return NULL
def get_invalid_token(line):
    invalid_token_match = re.match(UNAVAILABLE_TOKENS_REGEX, line)
    return invalid_token_match.group() if invalid_token_match else None

# Return all valid tokens if any exist
def get_valid_tokens(line):
    return re.findall(AVAILABLE_TOKENS_REGEX, line)

# Turn line into a vector of tokens
def tokenize_line(line):
    invalid_token = get_invalid_token(line)
    if invalid_token:
        print("Invalid Token: " + invalid_token)
        quit(2)
    valid_tokens = get_valid_tokens(line)
    print(valid_tokens)

# Evaluate input
def evaluate_input(line):
    if line == EXIT:
        quit(1)
    tokenize_line(line)

# Take in a line of input from std_in
def get_input():
    return input("> ")

# Take in input and evalutate the input
def driver():
    while True:
        line = get_input()
        evaluation = evaluate_input(line)

driver()
