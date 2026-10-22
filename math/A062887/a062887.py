from itertools import count


def a(n):
    m = 2 * n + 1
    if m % 125 == 0:
        return 0
    for length in count(1):
        candidates = sorted(int(''.join(str((d + 2 * i) % 10)
                                        for i in range(length - 1, -1, -1)))
                           for d in (1, 3, 5, 7, 9))
        for value in candidates:
            if value % m == 0:
                return value
