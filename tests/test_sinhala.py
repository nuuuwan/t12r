import unittest

from t12r import Sinhala, Token
from t12r.data.TestData import TestData

TEST_SI_TOKENS_PAIRS_SHORT = [
    (
        'කොග්ගල වූ කලි',
        [
            Token('ko'),
            Token('g'),
            Token('ga'),
            Token('la'),
            Token.SPACE,
            Token('vuu'),
            Token.SPACE,
            Token('ka'),
            Token('li'),
        ],
    ),
    (
        'මුහුදින්ද',
        [
            Token('mu'),
            Token('hu'),
            Token('di'),
            Token('n'),
            Token('da'),
        ],
    ),
    (
        ' විද්‍යා,',
        [Token.SPACE, Token('vi'), Token('dyaa'), Token(',')],
    ),
]

SI = Sinhala()


class TestSinhala(unittest.TestCase):
    def test_to_tokens(self):
        for text_si, tokens in TEST_SI_TOKENS_PAIRS_SHORT:
            print('-' * 32)
            print(text_si, tokens)
            self.assertEqual(tokens, SI.to_tokens(text_si))

    def test_from_tokens(self):
        for text_si, tokens in TEST_SI_TOKENS_PAIRS_SHORT:
            print('-' * 32)
            print(tokens, text_si)
            self.assertEqual(text_si, SI.from_tokens(tokens))

    def test_transliterate(self):
        for word_list in TestData.SI_LINES_IDX.values():
            for text_si in word_list:
                if not text_si:
                    continue
                text_en = SI.transliterate(text_si)
                print('-' * 32)
                print(text_si)
                print('')
                print(text_en)

                text_en_ascii = text_en.encode("ascii", "ignore").decode()
                self.assertEqual(text_en, text_en_ascii)

                text_si2 = SI.from_tokens(SI.to_tokens(text_si))
                print('')
                print(text_si2)
                self.assertEqual(text_si, text_si2)
