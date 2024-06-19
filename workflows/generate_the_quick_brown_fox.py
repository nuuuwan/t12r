import os

from utils import File, Log

from t12r import TestData

log = Log('generate_the_quick_brown_fox')

MIN_WORD_LEN = 3


def generate_the_quick_brown_fox():
    c_set = set()
    word_list = []
    while True:
        info_list = []
        for word in TestData.WORD_LIST:
            c_set_for_word = set([c for c in word])
            n = len(c_set_for_word)
            if n < MIN_WORD_LEN:
                continue

            new_c_set = c_set_for_word - c_set
            n_new = len(new_c_set)
            p_new = n_new / n

            info = dict(
                word=word,
                n=n,
                p_new=p_new,
                new_c_set=new_c_set,
            )
            info_list.append(info)

        sorted_info_list = sorted(
            info_list, key=lambda x: (-x['p_new'], x['n'], word)
        )
        best_info = sorted_info_list[0]
        log.debug(best_info)
        if best_info['p_new'] == 0:
            log.error(f'No more words to add {len(c_set)}')
            break
        c_set = c_set | best_info['new_c_set']
        word_list.append(best_info['word'])

    n_unique_chars = len(c_set)
    n_chars = len(''.join(word_list))
    file_path = os.path.join(
        'data', f'the_quick_brown_fox-{n_unique_chars}.txt'
    )
    File(file_path).write_lines(word_list)
    log.info(
        f'Wrote {n_unique_chars:,} unique unicode chars '
        + f'({len(word_list):,} words, {n_chars:,} chars) to {file_path}'
    )

    n_chars_running = 0
    words_in_line = []
    for word in word_list:
        words_in_line.append(word)
        chars = [c for c in word]
        n_chars_running += len(chars)
        if n_chars_running > 27:
            print(' '.join(words_in_line) + ',')
            words_in_line = []
            n_chars_running = 0
    print(' '.join(words_in_line) + '...')


if __name__ == "__main__":
    generate_the_quick_brown_fox()
