INTEGER = "INTEGER"
PLUS = "PLUS"
MINUS = "MINUS"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"
VARIABLE = "VARIABLE"
STRING = "STRING"
EQUAL = "EQUAL"
DOUBLE_EQUAL = "DOUBLE_EQUAL"
IF = "IF"
ELSE = "ELSE"
FOR = "FOR"
WHILE = "WHILE"

TOKEN_REGEXES = {
    # Data types
    INTEGER: "\d+",
    VARIABLE: "_*\w+_*",
    STRING: "\".*\"|'.*'",

    # Arithmetic Operators
    PLUS: "\+",
    MINUS: "-",

    # Assignments
    EQUAL: "=",
    DOUBLE_EQUAL: "==",

    # Arithmetic Operators
    MULTIPLY: "*",
    DIVIDE: "/",

    # Conditionals
    IF: "if",
    ELSE: "else",

    # Loops
    WHILE: "while",
    FOR: "for"
}

AVAILABLE_TOKENS = [
    INTEGER,
    PLUS
]

def unavailable_token_regex():
    return "[^"+("".join(all_available_token_regexes()))+"]"

def filtered_available_tokens():
    return { key:value for (key,value) in TOKEN_REGEXES.items() if key  in AVAILABLE_TOKENS}

def all_available_token_regexes():
    return list(filtered_available_tokens().values())

def available_token_regex():
    return "|".join(all_available_token_regexes())
