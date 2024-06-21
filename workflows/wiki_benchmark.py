import json

from t12r import Sinhala, WikiBenchmark


def main():
    si = Sinhala()

    wb = WikiBenchmark(si.transliterate, si.inverse_transliterate)

    info = wb.benchmark(n_max=100)
    print(json.dumps(info, indent=4))


if __name__ == "__main__":
    main()
