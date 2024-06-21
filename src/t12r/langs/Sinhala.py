from utils import Log

from t12r.langs.Lang import Lang

log = Log('Sinhala')


class Sinhala(
    Lang,
):
    def __init__(self):
        super().__init__("si", "Sinhala")

    def transliterate(self, text: str) -> str:
        return Sinhala._generic_transliterate(
            text,
            0,
            1,
        )

    def inverse_transliterate(self, text: str) -> str:
        return Sinhala._generic_transliterate(
            text,
            1,
            0,
        )
