from functools import cache


@cache
def long(x: str) -> str:
    return x * 2


@cache
def aspirate(x: str) -> str:
    return x + 'h'


@cache
def nasal(x: str) -> str:
    if x == '':
        return 'n'

    return x + '-n'


@cache
def prenasal(x: str) -> str:
    return 'n-' + x


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
        ('ඞ', nasal('g-')),
        ('ඟ', prenasal('g')),
        #
        ('ච', 'c'),
        ('ඡ', aspirate('c')),
        ('ජ', 'j'),
        ('ඣ', aspirate('j')),
        ('ඤ', nasal('j')),
        ('ඥ', 'jhn'),
        ('ඦ', prenasal('j')),
        #
        ('ට', 'q'),
        ('ඨ', aspirate('q')),
        ('ඩ', 'z'),
        ('ඪ', aspirate('z')),
        ('ණ', nasal('h')),
        ('ඬ', prenasal('z')),
        #
        ('ත', 't'),
        ('ථ', aspirate('t')),
        ('ද', 'd'),
        ('ධ', aspirate('d')),
        ('න', nasal('')),
        ('ඳ', prenasal('d')),
        #
        ('ප', 'p'),
        ('ඵ', aspirate('p')),
        ('බ', 'b'),
        ('භ', aspirate('b')),
        ('ම', 'm'),  # nasal
        ('ඹ', 'm-b'),  # prenasal
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
        ('ක්‍ව', 'k-v'),
        ('ක්‍ෂ', 'k-x'),
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
        ('්', ''),
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
