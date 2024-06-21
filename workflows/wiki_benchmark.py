from t12r import Sinhala, WikiBenchmark


def main():
    si = Sinhala()

    wb = WikiBenchmark(si.transliterate, si.inverse_transliterate)

    wb.benchmark()


if __name__ == "__main__":
    main()
