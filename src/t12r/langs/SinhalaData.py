class SinhalaData:
    CONSONANT_TO_TOKEN_CHAR = {
        'ක': 'k',
        'ඛ': 'kh',
        'ග': 'g',
        'ඝ': 'gh',
        'ඞ': 'gn',
        'ඟ': 'ng',
        #
        'ච': 'ch',
        'ඡ': 'chh',
        'ජ': 'j',
        'ඣ': 'jh',
        'ඤ': 'jn',
        'ඥ': 'nj',
        'ඦ': 'nj',
        #
        'ට': 't',
        'ඨ': 'th',
        'ඩ': 'd',
        'ඪ': 'dh',
        'ණ': 'n',
        'ඬ': 'nd',
        #
        'ත': 'th',
        'ථ': 'thh',
        'ද': 'dh',
        'ධ': 'dhh',
        'න': 'n',
        'ඳ': 'ndh',
        #
        'ප': 'p',
        'ඵ': 'ph',
        'බ': 'b',
        'භ': 'bh',
        'ම': 'm',
        'ඹ': 'mb',
        #
        'ය': 'y',
        'ර': 'r',
        'ල': 'l',
        'ව': 'v',
        'ශ': 'sh',
        'ෂ': 'shh',
        'ස': 's',
        'හ': 'h',
        'ළ': 'lh',
        'ෆ': 'f',
    }
    DIACRITIC_TO_TOKEN_CHAR = {
        '්': '',
        None: 'a',
        'ා': 'aa',
        'ැ': 'ae',
        'ෑ': 'aae',
        'ි': 'i',
        'ී': 'ii',
        'ු': 'u',
        'ූ': 'uu',
        'ෘ': 'ru',
        'ෙ': 'e',
        'ේ': 'ee',
        'ෛ': 'ai',
        'ො': 'o',
        'ෝ': 'oo',
        'ෞ': 'au',
        'ෟ': 'ru',
        'ෲ': 'ruu',
        'ෳ': 'ruu',
        '෴': 'ruu',
    }

    VOWEL_TO_TOKEN_CHAR = {
        'අ': 'a',
        'ආ': 'aa',
        'ඇ': 'ae',
        'ඈ': 'aae',
        'ඉ': 'i',
        'ඊ': 'ii',
        'උ': 'u',
        'ඌ': 'uu',
        'එ': 'e',
        'ඒ': 'ee',
        'ඔ': 'o',
        'ඕ': 'oo',
        'ඖ': 'au',
        'ඍ': 'ru',
        'ඎ': 'ruu',
        'ඏ': 'ae',
        'ඐ': 'ai',
        'ඓ': 'ai',
    }

    CONSONANTS = list(CONSONANT_TO_TOKEN_CHAR.keys())
    VOWELS = list(VOWEL_TO_TOKEN_CHAR.keys())
    DIACRITICS = list(DIACRITIC_TO_TOKEN_CHAR.keys())
