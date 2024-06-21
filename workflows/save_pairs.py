import os

from utils import JSONFile, Log

from t12r import Pairs

log = Log('save_pairs')


def main():
    i_src, i_dst = 0, 1
    pairs = Pairs.get_pairs(i_src, i_dst)
    output_path = os.path.join('data', 'pairs.json')
    JSONFile(output_path).write(pairs)
    log.info(f'Wrote {len(pairs)} pairs to {output_path}')


if __name__ == "__main__":
    main()
