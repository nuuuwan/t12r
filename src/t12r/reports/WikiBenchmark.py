import os

from utils import File, Log

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

    def benchmark_wiki_page(self, file_name: str) -> dict:
        print('-' * 32)
        file_path = os.path.join(self.DIR_WIKI_PAGES, file_name)
        text_si = File(file_path).read()
        print(text_si)
        text_en = self.func_transliterate(text_si)
        print()
        print(text_en)
        text_si2 = self.func_inverse_transliterate(text_en)
        text_en_ascii = text_en.encode('ascii', 'ignore').decode()

        is_ascii = text_en == text_en_ascii
        is_unambiguous = text_si == text_si2

        return dict(
            file_name=file_name,
            is_ascii=is_ascii,
            is_unambiguous=is_unambiguous,
        )

    def benchmark(self):
        info_list = []
        for file_name in os.listdir(self.DIR_WIKI_PAGES):
            if not file_name.endswith('.txt'):
                continue
            info = self.benchmark_wiki_page(file_name)
            info_list.append(info)
            break
        n = len(info_list)
        log.info(f'Benchmarked {n} wiki pages')

        return info_list
