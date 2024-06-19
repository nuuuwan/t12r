from utils import Log

from t12r.core import Token
from t12r.langs.Lang import Lang
from t12r.langs.SinhalaData import SinhalaData

log = Log('Sinhala')

# References
#  - https://en.wikipedia.org/wiki/Sinhala_script


class Sinhala(Lang, SinhalaData):
    def __init__(self):
        super().__init__("si", "Sinhala")

    @staticmethod
    def is_vowel(c: str) -> bool:
        return c and (c in Sinhala.VOWELS)

    @staticmethod
    def is_consonant(c: str) -> bool:
        return c and (c in Sinhala.CONSONANTS)

    @staticmethod
    def is_vowel_diacritic(c: str) -> bool:
        return c and (c in Sinhala.DIACRITICS)

    @staticmethod
    def is_sinhala(c: str) -> bool:
        return (
            Sinhala.is_vowel(c)
            or Sinhala.is_consonant(c)
            or Sinhala.is_vowel_diacritic(c)
        )

    @staticmethod
    def get_vowel_token(c: str) -> Token:
        c_token = Sinhala.VOWEL_TO_TOKEN_CHAR.get(c, Token.UNKNOWN)
        return Token(c_token)

    def get_consonant_token(c_consonant: str, c_diacritic: str):
        c_token_consonant = Sinhala.CONSONANT_TO_TOKEN_CHAR.get(
            c_consonant, Token.UNKNOWN
        )
        c_token_diacritic = Sinhala.DIACRITIC_TO_TOKEN_CHAR.get(
            c_diacritic, Token.UNKNOWN
        )
        return Token(c_token_consonant + c_token_diacritic)

    def tokenize(self, text: str) -> list[Token]:
        token_list = []
        for i, c in enumerate(text):
            c_next = text[i + 1] if i + 1 < len(text) else None
            # log.debug(f'{i}): "{c}", "{c_next}"')

            if not Sinhala.is_sinhala(c):
                token_list.append(Token(c))
            elif Sinhala.is_vowel(c):
                token_list.append(Sinhala.get_vowel_token(c))
            elif Sinhala.is_consonant(c):
                if Sinhala.is_vowel_diacritic(c_next):
                    token_list.append(Sinhala.get_consonant_token(c, c_next))
                elif not Sinhala.is_sinhala(c_next) or Sinhala.is_consonant(
                    c_next
                ):
                    token_list.append(Sinhala.get_consonant_token(c, None))
        # log.debug(f'{text} -> {token_list}')
        return token_list

    def transliterate(self, text: str) -> str:
        token_list = self.tokenize(text)
        s = ''.join([token.chars for token in token_list])
        log.debug(f'"{text}" -> "{s}"')
        return s
