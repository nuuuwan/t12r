from t12r import Sinhala, TestData


def main():
    c_to_n = {}
    for text_si, _ in TestData.SI_EN_PAIRS:
        for c in text_si:
            c_to_n[c] = c_to_n.get(c, 0) + 1

    for c in Sinhala.SINHALA_ALL_UNICODE:
        n = c_to_n.get(c, 0)
        if n == 0:
            print(c)


if __name__ == "__main__":
    main()
