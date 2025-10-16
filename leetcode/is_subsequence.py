"""
Задача: https://leetcode.com/problems/is-subsequence/
Подсказки:
"""


class Solution(object):
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ("abc","ahbgdc",True),
        ("axc","ahbgdc",False),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.isSubsequence(x,y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {y=} -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')