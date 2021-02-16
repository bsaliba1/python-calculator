class tokenRegexes:
    def __init__(self):
        self.INTEGER = "INTEGER"
        self.PLUS = "PLUS"
        self.MINUS = "MINUS"
        self.MULTIPLY = "MULTIPLY"
        self.DIVIDE = "DIVIDE"
        self.VARIABLE = "VARIABLE"
        self.STRING = "STRING"
        self.EQUAL = "EQUAL"
        self.DOUBLE_EQUAL = "DOUBLE_EQUAL"
        self.IF = "IF"
        self.ELSE = "ELSE"
        self.FOR = "FOR"
        self.WHILE = "WHILE"

        self.TOKEN_REGEXES = {
            # Data types
            self.INTEGER: "\d+",
            self.VARIABLE: "_*\w+_*",
            self.STRING: "\".*\"|'.*'",

            # Arithmetic Operators
            self.PLUS: "\+",
            self.MINUS: "-",

            # Assignments
            self.EQUAL: "=",
            self.DOUBLE_EQUAL: "==",

            # Arithmetic Operators
            self.MULTIPLY: "*",
            self.DIVIDE: "/",

            # Conditionals
            self.IF: "if",
            self.ELSE: "else",

            # Loops
            self.WHILE: "while",
            self.FOR: "for"
        }

        self.AVAILABLE_TOKENS = [
            self.INTEGER,
            self.PLUS
        ]

        self.AVAILABLE_TOKEN_REGEXES = { key:value for (key,value) in self.TOKEN_REGEXES.items() if key  in self.AVAILABLE_TOKENS}

        self.ALL_AVAILABLE_TOKENS_REGEXES = list(self.AVAILABLE_TOKEN_REGEXES.values())
        self.UNAVAILABLE_TOKENS_REGEX = "[^"+("".join(self.ALL_AVAILABLE_TOKENS_REGEXES))+"]"
        self.AVAILABLE_TOKENS_REGEX = "|".join(self.ALL_AVAILABLE_TOKENS_REGEXES)
