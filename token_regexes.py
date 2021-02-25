class TokenRegexes:
    integer = 11
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

    @classmethod
    def unavailable_token_regex(cls):
        return "[^"+("".join(cls.all_available_token_regexes()))+"]"

    @classmethod
    def filtered_available_tokens(cls):
        return { key:value for (key,value) in cls.TOKEN_REGEXES.items() if key  in cls.AVAILABLE_TOKENS}

    @classmethod
    def all_available_token_regexes(cls):
        return list(cls.filtered_available_tokens().values())

    @classmethod
    def available_token_regex(cls):
        return "|".join(cls.all_available_token_regexes())
