def sorted_len(x_list):
    return sorted(x_list, key=lambda x: (-len(x), x))


class SinhalaEnglishData:
    CONSONANTS_PAIRS = [
        ('ක', 'k'),
        ('ඛ', 'kh'),
        ('ග', 'g'),
        ('ඝ', 'gh'),
        ('ඞ', 'gn'),
        ('ඟ', 'ng'),
        #
        ('ච', 'ch'),
        ('ඡ', 'chh'),
        ('ජ', 'j'),
        ('ඣ', 'jh'),
        ('ඤ', 'jn'),
        ('ඥ', 'nj'),
        ('ඦ', 'nj'),
        #
        ('ට', 't'),
        ('ඨ', 'th'),
        ('ඩ', 'd'),
        ('ඪ', 'dh'),
        ('ණ', 'n'),
        ('ඬ', 'nd'),
        #
        ('ත', 'th'),
        ('ථ', 'thh'),
        ('ද', 'dh'),
        ('ධ', 'dhh'),
        ('න', 'n'),
        ('ඳ', 'ndh'),
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
        ('ෂ', 'shh'),
        ('ස', 's'),
        ('හ', 'h'),
        ('ළ', 'lh'),
        ('ෆ', 'f'),
    ]
    DIACRITIC_PAIRS = [
        ('්', ''),
        (None, 'a'),
        ('ා', 'aa'),
        ('ැ', 'ae'),
        ('ෑ', 'aae'),
        ('ි', 'i'),
        ('ී', 'ii'),
        ('ු', 'u'),
        ('ූ', 'uu'),
        ('ෘ', 'ru'),
        ('ෙ', 'e'),
        ('ේ', 'ee'),
        ('ෛ', 'ai'),
        ('ො', 'o'),
        ('ෝ', 'oo'),
        ('ෞ', 'au'),
        ('ෟ', 'ru'),
        ('ෲ', 'ruu'),
        ('ෳ', 'ruu'),
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
        ('එ', 'e'),
        ('ඒ', 'ee'),
        ('ඔ', 'o'),
        ('ඕ', 'oo'),
        ('ඖ', 'au'),
        ('ඍ', 'ru'),
        ('ඎ', 'ruu'),
        ('ඏ', 'ae'),
        ('ඐ', 'ai'),
        ('ඓ', 'ai'),
    ]

    SINHALA_CONSONANTS = [pair[0] for pair in CONSONANTS_PAIRS]
    SINHALA_VOWELS = [pair[0] for pair in VOWEL_PAIRS]
    SINHALA_DIACRITICS = [pair[0] for pair in DIACRITIC_PAIRS]

    SINHALA_TO_ENGLISH_CONSONANT = dict(CONSONANTS_PAIRS)
    SINHALA_TO_ENGLISH_VOWEL = dict(VOWEL_PAIRS)
    SINHALA_TO_ENGLISH_DIACRITIC = dict(DIACRITIC_PAIRS)

    ENGLISH_CONSONANTS = sorted_len([pair[1] for pair in CONSONANTS_PAIRS])
    ENGLISH_VOWELS = sorted_len([pair[1] for pair in VOWEL_PAIRS])
    ENGLISH_DIACRITICS = sorted_len([pair[1] for pair in DIACRITIC_PAIRS])

    ENGLISH_TO_SINHALA_CONSONANT = {
        v: k for k, v in SINHALA_TO_ENGLISH_CONSONANT.items()
    }
    ENGLISH_TO_SINHALA_VOWEL = {
        v: k for k, v in SINHALA_TO_ENGLISH_VOWEL.items()
    }
    ENGLISH_TO_SINHALA_DIACRITIC = {
        v: k for k, v in SINHALA_TO_ENGLISH_DIACRITIC.items()
    }
