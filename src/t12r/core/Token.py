class Token:
    DELIM = '_'

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

    @staticmethod
    def to_str(tokens: list) -> str:
        s = Token.DELIM.join([token.chars for token in tokens])
        s = s.replace(Token.DELIM + ' ' + Token.DELIM, ' ')
        return s

    @staticmethod
    def from_str(s: str) -> list:
        s = s.replace(' ', Token.DELIM + ' ' + Token.DELIM)
        return [Token(char) for char in s.split(Token.DELIM)]


Token.SPACE = Token(' ')
Token.UNKNOWN = Token('?')
