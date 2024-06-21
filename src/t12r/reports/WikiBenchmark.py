import os
import random
import re

from utils import File, Log

from t12r.langs.Diff import Diff

log = Log('WikiBenchmark')


class WikiBenchmark:
    DIR_WIKI_PAGES = os.path.join('data', 'wiki-pages')

    def __init__(
        self,
        func_transliterate: callable,
        func_inverse_transliterate: callable,
    ):
        self.func_transliterate = func_transliterate
        self.func_inverse_transliterate = func_inverse_transliterate

    @staticmethod
    def clean(s):
        SINHALA_UNICODE_RANGE = r'[^\u0D80-\u0DFF]'
        s = re.sub(SINHALA_UNICODE_RANGE, ' ', s)
        s = re.sub(r'\s+', ' ', s)
        return s.strip()

    @property
    def file_names(self) -> list[str]:
        return [
            file_name
            for file_name in os.listdir(self.DIR_WIKI_PAGES)
            if file_name.endswith('.txt')
        ]

    def benchmark_wiki_page(self, file_name: str) -> dict:
        file_path = os.path.join(self.DIR_WIKI_PAGES, file_name)
        text_si_original = File(file_path).read()
        text_si = WikiBenchmark.clean(text_si_original)
        text_en = self.func_transliterate(text_si)
        text_si2 = self.func_inverse_transliterate(text_en)

        is_unambiguous = text_si == text_si2
        if not is_unambiguous:
            print(Diff(text_si, text_si2))
            raise Exception('Unambiguous transliteration failed')

        n_text_si = len(text_si)
        n_text_en = len(text_en)

        return dict(
            file_name=file_name,
            is_unambiguous=is_unambiguous,
            n_text_si=n_text_si,
            n_text_en=n_text_en,
        )

    def aggregage(info_list: list[dict]) -> dict:
        n = len(info_list)

        n_unambiguous = sum(info['is_unambiguous'] for info in info_list)
        n_text_si = sum(info['n_text_si'] for info in info_list)
        n_text_en = sum(info['n_text_en'] for info in info_list)

        p_unambiguous = n_unambiguous / n
        p_si_to_en = n_text_en / n_text_si
        return dict(
            n=n,
            p_unambiguous=p_unambiguous,
            n_text_si=n_text_si,
            n_text_en=n_text_en,
            p_si_to_en=p_si_to_en,
        )

    def benchmark(self, n_max: int):
        info_list = []
        file_names = self.file_names
        random.shuffle(file_names)
        file_names = file_names[:n_max]

        n = len(file_names)
        for i, file_name in enumerate(file_names, start=1):
            log.debug(f'{i}/{n}) {file_name}')
            info = self.benchmark_wiki_page(file_name)
            info_list.append(info)

        n = len(info_list)
        log.info(f'Benchmarked {n} wiki pages')

        aggregate_info = WikiBenchmark.aggregage(info_list)

        return aggregate_info
