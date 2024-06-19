from utils import File, Log

from t12r.data import TestData
from t12r.langs import Sinhala

log = Log('ReadMe')


class ReadMe:
    @property
    def path(self) -> str:
        return 'README.md'

    @property
    def lines_examples(self) -> list[str]:
        lines = []
        si = Sinhala()

        for file_name, word_list in TestData.SI_LINES_IDX.items():
            title = file_name.replace('_', ' ').title()
            lines.extend(
                [
                    '### ' + title,
                    '',
                ]
            )
            for si_word in word_list:
                if len(si_word) == 0:
                    continue
                en_word = si.transliterate(si_word)
                lines.extend(
                    [
                        si_word,
                        '',
                        '> ' + en_word,
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
