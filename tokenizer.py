import token_regexes

class tokenizer
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
