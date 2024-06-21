from functools import cache

DASH_CHAR = ''
NO_VOWEL_CHAR = ''
ASPIRATE_CHAR = 'h'
LONG_CHAR = '+'


@cache
def long(x: str) -> str:
    assert x
    return x + LONG_CHAR


@cache
def bracket(x):
    assert x
    return f'({x})'


@cache
def aspirate(x: str) -> str:
    assert x
    return bracket(x + ASPIRATE_CHAR)


@cache
def upper(x: str) -> str:
    return aspirate(x)


@cache
def nasal(x: str) -> str:
    assert x
    return bracket(x + 'n')


@cache
def prenasal(x: str) -> str:
    assert x
    return bracket('n' + x)


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
        ('අං', '(an)'),
        ('අඃ', '(ah)'),
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
        ('ණ', upper('n')),  # nasal
        ('ඬ', prenasal('z')),
        #
        ('ත', 't'),
        ('ථ', aspirate('t')),
        ('ද', 'd'),
        ('ධ', aspirate('d')),
        ('න', 'n'),  # nasal
        ('ඳ', prenasal('d')),
        #
        ('ප', 'p'),
        ('ඵ', aspirate('p')),
        ('බ', 'b'),
        ('භ', aspirate('b')),
        ('ම', 'm'),  # nasal
        ('ඹ', '(mb)'),  # prenasal
        #
        ('ය', 'y'),
        ('ර', 'r'),
        ('ල', 'l'),
        ('ව', 'v'),
        ('ශ', upper('s')),
        ('ෂ', 'x'),
        ('ස', 's'),
        ('හ', 'h'),
        ('ළ', upper('l')),
        ('ෆ', 'f'),
        # conjunct/complex
        ('ක්‍ව', '(kv)'),
        ('ක්‍ෂ', '(kx)'),
    ]

    DIACRITIC_PAIRS = [
        #
        ('්', NO_VOWEL_CHAR),
        ('ා', long('a')),
        ('ැ', 'ae'),
        ('ෑ', long('ae')),
        ('ි', 'i'),
        ('ී', long('i')),
        ('ු', 'u'),
        ('ූ', long('u')),
        #
        ('ෙ', 'e'),
        ('ේ', long('e')),
        ('ෛ', 'ai'),
        ('ො', 'o'),
        ('ෝ', long('o')),
        ('ෞ', 'au'),
        #
        ('ෘ', '(ru)'),
        #
        ('ං', '(an)'),
        ('ඃ', '(ah)'),
    ]

    CONSONANTS_PLUS_DIACRITIC_PAIRS = [
        ('කෘ', '(kru)'),
        ('කෲ', '(kruu)'),
        ('පෘ', '(pru)'),
        ('බ්‍රි', '(bri)'),
    ]
