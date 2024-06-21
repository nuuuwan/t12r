from utils import Log

from t12r.langs.Pairs import Pairs

log = Log('Lang')


class Lang:
    def __init__(self, iso_code: str, name: str):
        self.iso_code = iso_code
        self.name = name

    @staticmethod
    def _generic_transliterate(
        text: str,
        i_src: int,
        i_dst: int,
    ) -> str:
        if len(text) == 0:
            return ''

        pairs = Pairs.get_pairs(i_src, i_dst)
        for pair in pairs:
            text_src, text_dst = pair
            if text.startswith(text_src):
                return text_dst + Lang._generic_transliterate(
                    text[len(text_src):],
                    i_src,
                    i_dst,
                )

        return text[0] + Lang._generic_transliterate(
            text[1:],
            i_src,
            i_dst,
        )
