from functools import cache

DASH_CHAR = ''
NO_VOWEL_CHAR = 'w'


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

    return x + DASH_CHAR + 'n'


@cache
def prenasal(x: str) -> str:
    return (x * 2) + DASH_CHAR + 'n'


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
        ('ඞ', nasal(f'g{DASH_CHAR}')),
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
        ('ණ', nasal('z')),
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
        ('ඹ', f'm{DASH_CHAR}b'),  # prenasal
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
        ('ක්‍ව', f'k{DASH_CHAR}v'),
        ('ක්‍ෂ', f'k{DASH_CHAR}x'),
    ]

    DIACRITIC_PAIRS = [
        #
        ('්', NO_VOWEL_CHAR),
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
        ('කෘ', 'kru'),
        ('කෲ', 'kruu'),
        ('පෘ', 'pru'),
        ('බ්‍රි', 'bri'),
    ]
