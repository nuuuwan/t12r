class Token:
    def __init__(self, chars: str):
        self.chars = chars

    def __str__(self) -> str:
        return f'Token<"{self.chars}">'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Token):
            return self.chars == value.chars
        return False


Token.SPACE = Token(' ')
Token.UNKNOWN = Token('?')
