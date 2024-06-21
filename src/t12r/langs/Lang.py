from utils import Log

log = Log('Lang')


class Lang:
    def __init__(self, iso_code: str, name: str):
        self.iso_code = iso_code
        self.name = name

    @staticmethod
    def _generic_transliterate(
        text: str, pairs: list[tuple[str, str]]
    ) -> str:
        if not text:
            return ''

        for before, after in pairs:
            if text.startswith(before):
                return after + Lang._generic_transliterate(
                    text[len(before):],
                    pairs,
                )

        return text[0] + Lang._generic_transliterate(text[1:], pairs)
