from functools import cache

from utils import Log

from t12r.core import Token
from t12r.langs.Lang import Lang
from t12r.langs.SinhalaEnglishData import SinhalaEnglishData

log = Log('Sinhala')


class Sinhala(Lang, SinhalaEnglishData):
    def __init__(self):
        super().__init__("si", "Sinhala")

    @staticmethod
    @cache
    def is_vowel(c: str) -> bool:
        return c and (c in Sinhala.SINHALA_VOWELS)

    @staticmethod
    @cache
    def is_consonant(c: str) -> bool:
        return c and (c in Sinhala.SINHALA_CONSONANTS)

    @staticmethod
    @cache
    def is_vowel_diacritic(c: str) -> bool:
        return c and (c in Sinhala.SINHALA_DIACRITICS)

    @staticmethod
    @cache
    def is_sinhala(c: str) -> bool:
        return c and c in Sinhala.SINHALA_ALL_UNICODE

    @cache
    def get_consonant_token(c_consonant: str, c_diacritic: str):
        c_token_consonant = Sinhala.SINHALA_TO_ENGLISH_CONSONANT.get(
            c_consonant, Token.UNKNOWN
        )
        c_token_diacritic = Sinhala.SINHALA_TO_ENGLISH_DIACRITIC.get(
            c_diacritic, Token.UNKNOWN
        )
        return Token(c_token_consonant + c_token_diacritic)

    def to_tokens(self, text: str) -> list[Token]:
        if not text:
            return []

        for c in Sinhala.SINHALA_VOWELS:
            if text.startswith(c):
                j = len(c)
                c_token = Sinhala.SINHALA_TO_ENGLISH_VOWEL[c]
                return [Token(c_token)] + self.to_tokens(text[j:])

        for c in Sinhala.SINHALA_CONSONANTS:
            if text.startswith(c):
                c_token = Sinhala.SINHALA_TO_ENGLISH_CONSONANT[c]
                j = len(c)
                text_rem = text[j:]

                if text_rem:
                    for c_diacritic in Sinhala.SINHALA_DIACRITICS:
                        if not c_diacritic:
                            continue
                        if text_rem.startswith(c_diacritic):
                            c_token_diacritic = (
                                Sinhala.SINHALA_TO_ENGLISH_DIACRITIC[
                                    c_diacritic
                                ]
                            )
                            return [
                                Token(c_token + c_token_diacritic)
                            ] + self.to_tokens(text[len(c + c_diacritic):])

                return [Token(c_token + 'a')] + self.to_tokens(text[len(c):])

        return [Token(text[0])] + self.to_tokens(text[1:])

    def from_tokens(self, token_list: list[Token]) -> str:
        text = ''
        for i, token in enumerate(token_list):
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

        return text
