from utils import Log

from t12r.core import Token
from t12r.langs.Lang import Lang
from t12r.langs.SinhalaEnglishData import SinhalaEnglishData

log = Log('Sinhala')

# References
#  - https://en.wikipedia.org/wiki/Sinhala_script


class Sinhala(Lang, SinhalaEnglishData):
    def __init__(self):
        super().__init__("si", "Sinhala")

    @staticmethod
    def is_vowel(c: str) -> bool:
        return c and (c in Sinhala.SINHALA_VOWELS)

    @staticmethod
    def is_consonant(c: str) -> bool:
        return c and (c in Sinhala.SINHALA_CONSONANTS)

    @staticmethod
    def is_vowel_diacritic(c: str) -> bool:
        return c and (c in Sinhala.SINHALA_DIACRITICS)

    @staticmethod
    def is_sinhala(c: str) -> bool:
        return (
            Sinhala.is_vowel(c)
            or Sinhala.is_consonant(c)
            or Sinhala.is_vowel_diacritic(c)
        )

    @staticmethod
    def get_vowel_token(c: str) -> Token:
        c_token = Sinhala.SINHALA_TO_ENGLISH_VOWEL.get(c, Token.UNKNOWN)
        return Token(c_token)

    def get_consonant_token(c_consonant: str, c_diacritic: str):
        c_token_consonant = Sinhala.SINHALA_TO_ENGLISH_CONSONANT.get(
            c_consonant, Token.UNKNOWN
        )
        c_token_diacritic = Sinhala.SINHALA_TO_ENGLISH_DIACRITIC.get(
            c_diacritic, Token.UNKNOWN
        )
        return Token(c_token_consonant + c_token_diacritic)

    def to_tokens(self, text: str) -> list[Token]:
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

    def from_tokens(self, token_list: list[Token]) -> str:
        text = ''
        for i, token in enumerate(token_list):
            # log.debug(f'{i}): {token}')
            if token.chars in Sinhala.ENGLISH_VOWELS:
                c = Sinhala.ENGLISH_TO_SINHALA_VOWEL.get(token.chars)
                text += c
                continue

            has_consonant = False
            for c in Sinhala.ENGLISH_CONSONANTS:
                if token.chars.startswith(c):
                    c_consonant = Sinhala.ENGLISH_TO_SINHALA_CONSONANT.get(c)
                    c_diacritic = Sinhala.ENGLISH_TO_SINHALA_DIACRITIC.get(
                        token.chars[len(c):]
                    )
                    text += c_consonant
                    if c_diacritic:
                        text += c_diacritic
                    has_consonant = True
                    break
            if has_consonant:
                continue

            text += token.chars

        # log.debug(f'{token_list} -> {text}')
        return text
