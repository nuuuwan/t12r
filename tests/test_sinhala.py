import unittest

from TestData import TestData

from t12r import Sinhala, Token


class TestSinhala(unittest.TestCase):
    def test_tokenize(self):
        si = Sinhala()
        for text_si, token_list_expected in [
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
        ]:
            token_list_observed = si.tokenize(text_si)
            self.assertEqual(token_list_expected, token_list_observed)

    def test_transliterate(self):
        si = Sinhala()
        for text_si, text_en_expected in TestData.SI_EN_PAIRS:
            text_en_observed = si.transliterate(text_si)
            self.assertEqual(text_en_expected, text_en_observed)
