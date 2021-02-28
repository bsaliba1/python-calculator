import token_types

TOKEN_REGEXES = {
    # Data types
    token_types.INTEGER: "\d+",
    token_types.VARIABLE: "_*\w+_*",
    token_types.STRING: "\".*\"|'.*'",

    # Arithmetic Operators
    token_types.PLUS: "\+",
    token_types.MINUS: "-",

    # Assignments
    token_types.EQUAL: "=",
    token_types.DOUBLE_EQUAL: "==",

    # Arithmetic Operators
    token_types.MULTIPLY: "*",
    token_types.DIVIDE: "/",

    # Conditionals
    token_types.IF: "if",
    token_types.ELSE: "else",

    # Loops
    token_types.WHILE: "while",
    token_types.FOR: "for"
}

AVAILABLE_TOKENS = [
    token_types.INTEGER,
    token_types.PLUS
]

def unavailable_token_regex():
    return "[^"+("".join(all_available_token_regexes()))+"]"

def filtered_available_tokens():
    return { key:value for (key,value) in TOKEN_REGEXES.items() if key  in AVAILABLE_TOKENS}

def all_available_token_regexes():
    return list(filtered_available_tokens().values())

def available_token_regex():
    return "|".join(all_available_token_regexes())
