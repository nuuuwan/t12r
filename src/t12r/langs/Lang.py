from utils import Log

from t12r.langs.Pairs import Pairs

log = Log('Lang')


class Lang:
    def __init__(self, iso_code: str, name: str):
        self.iso_code = iso_code
        self.name = name

    @staticmethod
    def _generic_transliterate(
        text_all: str,
        i_src: int,
        i_dst: int,
    ) -> str:
        pairs = Pairs.get_pairs(i_src, i_dst)

        text_output = ''
        n = len(text_all)
        i_offset = 0
        while i_offset <= n - 1:
            text = text_all[i_offset:]

            found_match = False
            for pair in pairs:
                text_src, text_dst = pair
                if text.startswith(text_src):
                    text_output += text_dst
                    i_offset += len(text_src)
                    found_match = True
                    break
            if found_match:
                continue

            text_output += text[0]
            i_offset += 1

        return text_output
