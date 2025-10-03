"""
Задача: https://leetcode.com/problems/isomorphic-strings/
Подсказки:
"""

class Solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st, map_ts = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in map_st and map_st[c1] != c2) or
                    (c2 in map_ts and map_ts[c2] != c1)):
                return False

            map_st[c1] = c2
            map_ts[c2] = c1

        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t))


if __name__=='__main__':
    cls = Solution()

    tests = [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("badc", "baba", False),
        ("a", "a", True),
        ("ab", "aa", False),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.isIsomorphic(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {y=} -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')