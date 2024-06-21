import unittest

from t12r import Pairs


class TestPairs(unittest.TestCase):
    def test_get_pairs(self):
        pairs = Pairs.get_pairs(1, 0)
        i_vuu = pairs.index(('vuu', 'වූ'))
        i_vu = pairs.index(('vu', 'වු'))
        self.assertLess(i_vuu, i_vu)
