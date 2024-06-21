import unittest

from t12r import Sinhala
from t12r.data.TestData import TestData

SI = Sinhala()


class TestSinhala(unittest.TestCase):
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

                text_si2 = SI.inverse_transliterate(text_en)
                print('')
                print(text_si2)
                self.assertEqual(text_si, text_si2)
