from utils import Log

log = Log('Pairs')

# References
# - https://en.wikipedia.org/wiki/Sinhala_script
# -  https://si.wikipedia.org/wiki/Sinhala_(Unicode_block)


# Unused:
# - w
class Pairs:
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

    CONSONANTS_PLUS_DIACRITIC_PAIRS = [
        ('ඍ', 'sru'),
        ('කෘ', 'kru'),
        ('කෲ', 'kruu'),
        ('දෟ', 'dru'),
        ('පෘ', 'pru'),
        ('බ්‍රි', 'bri'),
    ]

    DIACRITIC_PAIRS = [
        #
        ('්', '-'),
        # ('$', 'a'),
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
        ('ං', 'ang'),
        ('ඃ', 'ak'),
        # HACK
        ('ාං', 'aang'),
        ('ිං', 'ing'),
        ('ෙං', 'eng'),
    ]

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

    @staticmethod
    def build_pairs():
        pairs = []
        pairs.extend(Pairs.VOWEL_PAIRS)

        for si_c, en_c in Pairs.CONSONANTS_PAIRS:
            pairs.append((si_c, en_c + 'a'))
            for si_d, en_d in Pairs.DIACRITIC_PAIRS:
                pairs.append((si_c + si_d, en_c + en_d))

        n = len(pairs)
        log.info(f'Generated {n} pairs.')

        pairs = sorted(pairs, key=lambda pair: (-len(pair[0]), pair[0]))

        return pairs
    
    
Pairs.PAIRS = Pairs.build_pairs()


if __name__ == "__main__":
    pairs = Pairs.PAIRS
    print(pairs[:10])
    print(pairs[-10:])
