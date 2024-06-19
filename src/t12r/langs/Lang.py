from utils import Log

from t12r.core import Token

log = Log('Lang')


class Lang:
    def __init__(self, iso_code: str, name: str):
        self.iso_code = iso_code
        self.name = name

    def to_tokens(self, text: str) -> list[Token]:
        raise NotImplementedError

    def transliterate(self, text: str) -> str:
        token_list = self.to_tokens(text)
        return Token.to_str(token_list)

    def inverse_transliterate(self, text: str) -> str:
        token_list = Token.from_str(text)
        return self.from_tokens(token_list)
