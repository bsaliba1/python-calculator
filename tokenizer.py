import re
import token_regexes
import token_types
from token import Token


# Turn line into a vector of tokens
def tokenize_line(line):
    invalid_tokens = __get_invalid_token_strings(line)
    if invalid_tokens:
        raise Exception("Invalid Tokens: " + ', '.join(invalid_tokens))
    else:
        valid_tokens = __get_valid_tokens(line)
        return valid_tokens

# private

# Return an invalid token strings if one exists in the line otherwise return NULL
def __get_invalid_token_strings(line):
    return re.findall(token_regexes.unavailable_token_regex(), line)

# Return all valid token strings if any exist
def __get_valid_token_strings(line):
    return re.findall(token_regexes.available_token_regex(), line)

# Turn token string representations into actual tokens
def __tokenize_strings(token_strings):
    tokens = []
    for token_string in token_strings:
        if token_string.isdigit():
            tokens.append(Token(token_types.INTEGER, int(token_string)))
        elif token_string == '+':
            tokens.append(Token(token_types.PLUS, token_string))

    return tokens

# Retrieve an array of valid tokens in a line of text
def __get_valid_tokens(line):
    token_strings = __get_valid_token_strings(line)
    tokens = __tokenize_strings(token_strings)
    return tokens
