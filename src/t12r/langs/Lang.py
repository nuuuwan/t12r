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

        i_offset = 0
        unique_char_str = Pairs.get_unique_char_str(i_src)
        while True:
            if i_offset >= len(text):
                return text

            if text[i_offset] in unique_char_str:
                return text[:i_offset] + Lang._generic_transliterate(
                    text[i_offset:],
                    i_src,
                    i_dst,
                )

            i_offset += 1
