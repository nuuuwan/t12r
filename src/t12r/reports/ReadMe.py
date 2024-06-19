from utils import File, Log

from t12r.data import TestData

log = Log('ReadMe')


class ReadMe:
    @property
    def path(self) -> str:
        return 'README.md'

    @property
    def lines_examples(self) -> list[str]:
        lines = []
        for pair in TestData.SI_EN_PAIRS:
            lines.extend(
                [
                    pair[0],
                    '',
                    '> ' + pair[1],
                    '',
                ]
            )
        return lines

    @property
    def lines(self) -> list[str]:
        return [
            '# සිංහල Transliteration',
            '',
            '## Examples',
            '',
        ] + self.lines_examples

    def build(self):
        File(self.path).write_lines(self.lines)
        log.info(f'Wrote {self.path}')
