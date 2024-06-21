from functools import cache

from utils import Log

# from t12r.langs.PairsDataFormal import PairsDataFormal
from t12r.langs.PairsDataTyping import PairsDataTyping

log = Log('Pairs')


# class Pairs(PairsDataFormal):
class Pairs(PairsDataTyping):
    @staticmethod
    @cache
    def get_expanded_consonant_pairs():
        pairs = []
        for si_c, en_c in Pairs.CONSONANTS_PAIRS:
            pairs.append((si_c, en_c))
            for si_v, en_v in [
                ('\u200dය', '(y)'),
                ('්\u200dර', '(r)'),
            ]:
                pairs.append((si_c + si_v, en_c + en_v))
        return pairs

    @staticmethod
    @cache
    def get_consonant_diacritic_pairs():
        pairs = []
        for si_c, en_c in Pairs.get_expanded_consonant_pairs():
            pairs.append((si_c, en_c + 'a'))
            for si_d, en_d in Pairs.DIACRITIC_PAIRS:
                pairs.append((si_c + si_d, en_c + en_d))
        return pairs

    @staticmethod
    @cache
    def build_pairs() -> list[tuple[str, str]]:
        pairs = []
        pairs.extend([(pair[0], ':' + pair[1]) for pair in Pairs.VOWEL_PAIRS])
        pairs.extend(
            [(' ' + pair[0], ' ' + pair[1]) for pair in Pairs.VOWEL_PAIRS]
        )

        pairs.extend(Pairs.CONSONANTS_PLUS_DIACRITIC_PAIRS)
        pairs.extend(Pairs.get_consonant_diacritic_pairs())

        log.info(f'Generated {len(pairs)} pairs.')
        return pairs

    @staticmethod
    @cache
    def get_pairs(i_src: int, i_dst: int) -> list[tuple[str, str]]:
        pairs = Pairs.build_pairs()
        pairs = [(pair[i_src], pair[i_dst]) for pair in pairs]
        pairs = sorted(
            pairs,
            key=lambda x: (-len(x[0]), x[0]),
        )
        return pairs
