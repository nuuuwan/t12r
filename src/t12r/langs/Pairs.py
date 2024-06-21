from functools import cache

from utils import Log

log = Log('Pairs')

# References
# - https://en.wikipedia.org/wiki/Sinhala_script
# -  https://si.wikipedia.org/wiki/Sinhala_(Unicode_block)


# Unused:
# - w
class Pairs:
    VOWEL_PAIRS = [
        ('අ', 'a'),
        ('ආ', 'aa'),
        ('ඇ', 'ae'),
        ('ඈ', 'aae'),
        ('ඉ', 'i'),
        ('ඊ', 'ii'),
        ('උ', 'u'),
        ('ඌ', 'uu'),
        #
        ('එ', 'e'),
        ('ඒ', 'ee'),
        ('ඓ', 'ai'),
        ('ඔ', 'o'),
        ('ඕ', 'oo'),
        ('ඖ', 'au'),
        #
        ('අං', 'ang'),
        ('අඃ', 'ak'),
    ]
    CONSONANTS_PAIRS = [
        ('ක', 'k'),
        ('ඛ', 'kh'),
        ('ග', 'g'),
        ('ඝ', 'gh'),
        ('ඞ', 'gn'),
        ('ඟ', 'ng'),
        #
        ('ච', 'c'),
        ('ඡ', 'ch'),
        ('ජ', 'j'),
        ('ඣ', 'jh'),
        ('ඤ', 'jn'),
        ('ඥ', 'jhn'),
        ('ඦ', 'nj'),
        #
        ('ට', 'q'),
        ('ඨ', 'qh'),
        ('ඩ', 'z'),
        ('ඪ', 'zh'),
        ('ණ', 'nh'),
        ('ඬ', 'nz'),
        #
        ('ත', 't'),
        ('ථ', 'th'),
        ('ද', 'd'),
        ('ධ', 'dh'),
        ('න', 'n'),
        ('ඳ', 'nd'),
        #
        ('ප', 'p'),
        ('ඵ', 'ph'),
        ('බ', 'b'),
        ('භ', 'bh'),
        ('ම', 'm'),
        ('ඹ', 'mb'),
        #
        ('ය', 'y'),
        ('ර', 'r'),
        ('ල', 'l'),
        ('ව', 'v'),
        ('ශ', 'sh'),
        ('ෂ', 'x'),
        ('ස', 's'),
        ('හ', 'h'),
        ('ළ', 'lh'),
        ('ෆ', 'f'),
        # conjunct/complex
        ('ක්‍ර', 'kr'),
        ('ක්‍ව', 'kv'),
        ('ක්‍ව', 'kw'),
        ('ක්‍ෂ', 'kx'),
        ('ඛ්‍ය', 'khy'),
        ('ජ්‍ය', 'jy'),
        ('ත්‍ය', 'ty'),
        ('ත්‍ර', 'tr'),
        ('ද්‍ය', 'dy'),
        ('ද්‍ර', 'dr'),
        ('න්‍ය', 'ny'),
        ('ප්‍ර', 'pr'),
        ('ම්‍ය', 'my'),
        ('ව්‍ය', 'vy'),
        ('ශ්‍ර', 'shr'),
    ]

    DIACRITIC_PAIRS = [
        #
        ('්', '-'),
        ('ා', 'aa'),
        ('ැ', 'ae'),
        ('ෑ', 'aae'),
        ('ි', 'i'),
        ('ී', 'ii'),
        ('ු', 'u'),
        ('ූ', 'uu'),
        #
        ('ෙ', 'e'),
        ('ේ', 'ee'),
        ('ෛ', 'ai'),
        ('ො', 'o'),
        ('ෝ', 'oo'),
        ('ෞ', 'au'),
        #
        ('ෘ', 'ru'),
        #
        ('ං', 'angg'),
        ('ඃ', 'akk'),
        # HACK
        ('ාං', 'aang'),
        ('ිං', 'ing'),
        ('ෙං', 'eng'),
    ]

    CONSONANTS_PLUS_DIACRITIC_PAIRS = [
        ('ඍ', 'sru'),
        ('කෘ', 'kru'),
        ('කෲ', 'kruu'),
        ('දෟ', 'dru'),
        ('පෘ', 'pru'),
        ('බ්‍රි', 'bri'),
    ]

    @staticmethod
    @cache
    def get_consonant_diacritic_pairs():
        pairs = []
        for si_c, en_c in Pairs.CONSONANTS_PAIRS:
            pairs.append((si_c, en_c + 'a'))
            for si_d, en_d in Pairs.DIACRITIC_PAIRS:
                pairs.append((si_c + si_d, en_c + en_d))
        return pairs

    @staticmethod
    @cache
    def build_pairs() -> list[tuple[str, str]]:
        pairs = []
        pairs.extend(Pairs.VOWEL_PAIRS)
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
