import unittest

from t12r import Sinhala, Token
from t12r.data.TestData import TestData

TEST_TEXT_SI = 'කොග්ගල වූ කලි'
TEST_TOKEN_LIST = [
    Token('ko'),
    Token('g'),
    Token('ga'),
    Token('la'),
    Token.SPACE,
    Token('vuu'),
    Token.SPACE,
    Token('ka'),
    Token('li'),
]


class TestSinhala(unittest.TestCase):
    def test_to_tokens(self):
        self.assertEqual(TEST_TOKEN_LIST, Sinhala().to_tokens(TEST_TEXT_SI))

    def test_from_tokens(self):
        self.assertEqual(TEST_TEXT_SI, Sinhala().from_tokens(TEST_TOKEN_LIST))

    def test_transliterate(self):
        si = Sinhala()
        for text_si, text_en in TestData.SI_EN_PAIRS:
            text_en2 = si.transliterate(text_si)
            self.assertEqual(text_en, text_en2)

            text_si2 = si.from_tokens(si.to_tokens(text_si))
            self.assertEqual(text_si, text_si2)

            print('-' * 32)
            print(text_si)
            print(text_en)
