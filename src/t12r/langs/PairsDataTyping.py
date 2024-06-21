from functools import cache


@cache
def long(x: str) -> str:
    return x * 2


@cache
def aspirate(x: str) -> str:
    return x + 'h'


class PairsDataTyping:
    VOWEL_PAIRS = [
        ('අ', 'a'),
        ('ආ', long('a')),
        ('ඇ', 'ae'),
        ('ඈ', long('ae')),
        ('ඉ', 'i'),
        ('ඊ', long('i')),
        ('උ', 'u'),
        ('ඌ', long('u')),
        #
        ('එ', 'e'),
        ('ඒ', long('e')),
        ('ඓ', 'ai'),
        ('ඔ', 'o'),
        ('ඕ', long('o')),
        ('ඖ', 'au'),
        #
        ('අං', 'ahn'),
        ('අඃ', 'ahh'),
    ]
    CONSONANTS_PAIRS = [
        ('ක', 'k'),
        ('ඛ', aspirate('k')),
        ('ග', 'g'),
        ('ඝ', aspirate('g')),
        ('ඞ', 'gn'),
        ('ඟ', 'ng'),
        #
        ('ච', 'c'),
        ('ඡ', aspirate('c')),
        ('ජ', 'j'),
        ('ඣ', aspirate('j')),
        ('ඤ', 'jn'),
        ('ඥ', 'jhn'),
        ('ඦ', 'nj'),
        #
        ('ට', 'q'),
        ('ඨ', aspirate('q')),
        ('ඩ', 'z'),
        ('ඪ', aspirate('z')),
        ('ණ', 'nh'),
        ('ඬ', 'nz'),
        #
        ('ත', 't'),
        ('ථ', aspirate('t')),
        ('ද', 'd'),
        ('ධ', aspirate('d')),
        ('න', 'n'),
        ('ඳ', 'nd'),
        #
        ('ප', 'p'),
        ('ඵ', aspirate('p')),
        ('බ', 'b'),
        ('භ', aspirate('b')),
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
