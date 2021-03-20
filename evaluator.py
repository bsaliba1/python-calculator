import token_types

class Evaluator:
    def __init__(self, tokens):
        self.pos = -1
        self.tokens = tokens
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        self.pos += 1
        return self.tokens[self.pos]

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(token_types.INTEGER)

        op = self.current_token
        self.eat(token_types.PLUS)

        right = self.current_token

        result = left.value + right.value

        return result
