import os
from utils import Console, File

from t12r import Sinhala


def main():
    s = Sinhala()
    temp_path =  os.path.join(os.environ['DIR_DESKTOP'], 't12r.chat.txt')
    lines = []
    while True:
        print('> ', end='')
        text = input()
        if text in ['exit', 'x', 'quit', 'q']:
            break
        text_en = text
        text_si = s.inverse_transliterate(text_en)
        lines.append(text_si)

        print()
        for line in lines:
            print(line)
        print()

        File(temp_path).write_lines(lines)
    os.startfile(temp_path)

if __name__ == "__main__":
    main()
