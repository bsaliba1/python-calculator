import re
import token_regexes

class Tokenizer:
    # Return an invalid token if one exists in the line otherwise return NULL
    @classmethod
    def get_invalid_token(cls, line):
        invalid_token_match = re.match(token_regexes.unavailable_token_regex(), line)
        return invalid_token_match.group() if invalid_token_match else None

    # Return all valid tokens if any exist
    @classmethod
    def get_valid_tokens(cls, line):
        return re.findall(token_regexes.available_token_regex(), line)

    # Turn line into a vector of tokens
    @classmethod
    def tokenize_line(cls, line):
        invalid_token = cls.get_invalid_token(line)
        if invalid_token:
            print("Invalid Token: " + invalid_token)
        else:
            valid_tokens = cls.get_valid_tokens(line)
            print(valid_tokens)
