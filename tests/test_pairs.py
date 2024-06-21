import unittest

from t12r import Pairs


class TestPairs(unittest.TestCase):
    def test_get_pairs(self):
        pairs = Pairs.get_pairs(1, 0)
        i_vuu = pairs.index(('vuu', 'වූ'))
        i_vu = pairs.index(('vu', 'වු'))
        self.assertLess(i_vuu, i_vu)

    def test_get_unique_char_str(self):
        unique_char_str_si = Pairs.get_unique_char_str(0)
        self.assertEqual(
            unique_char_str_si,
            'ංඃඅආඇඈඉඊඋඌඍඑඒඓඔඕඖ'
            + 'කඛගඝඞඟචඡජඣඤඥඦටඨඩඪණඬතථදධනඳපඵබභමඹ'
            + 'යරලවශෂසහළෆ්ාැෑිීුූෘෙේෛොෝෞෟෲ‍',
        )
        self.assertEqual(
            len(unique_char_str_si),
            76,
        )

        unique_char_str_en = Pairs.get_unique_char_str(1)
        self.assertEqual(
            unique_char_str_en,
            'abcdefghijklmnopqrstuvxyz~',
        )
        self.assertEqual(
            len(unique_char_str_en),
            26,
        )
