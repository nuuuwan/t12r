from utils import Log

from t12r.langs.Lang import Lang
from t12r.langs.Pairs import SinhalaEnglishData

log = Log('Sinhala')


class Sinhala(Lang, SinhalaEnglishData):
    def __init__(self):
        super().__init__("si", "Sinhala")

    def transliterate(self, text: str) -> str:
        return Sinhala._generic_transliterate(
            text,
            self.SI_AND_EN_PAIRS,
        )

    def inverse_transliterate(self, text: str) -> str:
        return Sinhala._generic_transliterate(
            text,
            self.EN_AND_SI_PAIRS,
        )
