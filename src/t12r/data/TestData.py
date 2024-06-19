import os
from functools import cache

from utils import File, Log

log = Log('TestData')


class TestData:
    @staticmethod
    def clean(line):
        line = ''.join(c for c in line if 3456 <= ord(c) <= 3583 or c == ' ')
        line = line.strip()
        return line

    @staticmethod
    def clean_data(file_name):
        file_path = os.path.join('data', file_name + '.txt')
        file = File(file_path)
        lines = file.read_lines()

        lines = [TestData.clean(line) for line in lines]
        lines = [line for line in lines if line]
        lines = list(set(lines))
        lines.sort()

        file.write_lines(lines)
        log.info(f'Cleaned {file_path}')

    @staticmethod
    @cache
    def read_data(file_name) -> list[str]:
        file_path = os.path.join('data', file_name + '.txt')
        lines = File(file_path).read_lines()
        n_lines = len(lines)
        log.debug(f'Read {n_lines} lines from {file_path}')
        return lines

    WORD_LIST = read_data('si-word-list')

    SI_LINES_SOURCES = [
        'national_anthem',
        'sri_lanka',
        'sri_lanka_history',
        'koggala',
        'the_quick_brown_fox',
    ]

    @staticmethod
    def get_si_lines_idx():
        return {
            file_name: TestData.read_data(file_name)
            for file_name in TestData.SI_LINES_SOURCES
        }


TestData.SI_LINES_IDX = TestData.get_si_lines_idx()
