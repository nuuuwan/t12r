def sorted_len(x_list):
    return sorted(x_list, key=lambda x: (-len(x), x))


# References
# - https://en.wikipedia.org/wiki/Sinhala_script
# -  https://si.wikipedia.org/wiki/Sinhala_(Unicode_block)


# Unused:
# - w
class SinhalaEnglishData:
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
        ('ඍ', 'sru'),
        ('කෘ', 'kru'),
        ('කෲ', 'kruu'),
        ('ක්‍ර', 'kr'),
        ('ක්‍ව', 'kv'),
        ('ක්‍ව', 'kw'),
        ('ක්‍ෂ', 'kx'),
        ('ව්‍ය', 'vy'),
        ('ඛ්‍ය', 'khy'),
        ('ජ්‍ය', 'jy'),
        ('ත්‍ය', 'ty'),
        ('ත්‍ර', 'tr'),
        ('දෟ', 'dru'),
        ('ද්‍ය', 'dy'),
        ('න්‍ය', 'ny'),
        ('පෘ', 'pru'),
        ('ප්‍ර', 'pr'),
        ('බ්‍රි', 'bri'),
        ('ම්‍ය', 'my'),
        ('ශ්‍ර', 'shr'),
        ('ද්‍ර', 'dra'),
    ]
    DIACRITIC_PAIRS = [
        #
        ('්', ''),
        (None, 'a'),
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

    SINHALA_CONSONANTS = sorted_len([pair[0] for pair in CONSONANTS_PAIRS])
    SINHALA_VOWELS = sorted_len([pair[0] for pair in VOWEL_PAIRS])
    SINHALA_DIACRITICS = sorted_len(
        [pair[0] for pair in DIACRITIC_PAIRS if pair[0]]
    )

    SINHALA_ALL_UNICODE = (
        ''.join(
            [
                c
                for c in SINHALA_CONSONANTS
                + SINHALA_VOWELS
                + SINHALA_DIACRITICS
                if c
            ]
        )
        + '\u200d'
    )

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


if __name__ == "__main__":
    print(SinhalaEnglishData.SINHALA_CONSONANTS)
