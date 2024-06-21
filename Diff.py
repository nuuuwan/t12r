class Diff:
    WINDOW = 5

    def __init__(self, a: str, b: str):
        self.a = a
        self.b = b

    @staticmethod
    def as_chars(s: str) -> list[str]:
        return list(s)

    @staticmethod
    def get_window(s: str, i: int) -> str:
        return '\n'.join(
            [
                s[i - Diff.WINDOW * 4: i + Diff.WINDOW * 4],
                str(Diff.as_chars(s[i - Diff.WINDOW: i + Diff.WINDOW])),
            ]
        )

    def __str__(self) -> str:
        if self.a == self.b:
            return ''

        i = 0
        while True:
            if self.a[i] == self.b[i]:
                i += 1
                continue

            return '\n'.join(
                [
                    f'{i=}',
                    Diff.get_window(self.a, i),
                    Diff.get_window(self.b, i),
                ]
            )
