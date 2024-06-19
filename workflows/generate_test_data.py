from t12r import Sinhala, TestData


def main():
    si = Sinhala()
    char_set = set()
    for text_si, _ in TestData.SI_EN_PAIRS:
        chars = set([c for c in text_si])
        new_chars = chars - char_set
        text_en = si.transliterate(text_si)
        print(f'("{text_si}", "{text_en}"), # {new_chars}')
        char_set = char_set.union(chars)


if __name__ == "__main__":
    main()
