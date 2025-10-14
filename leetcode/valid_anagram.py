"""
Задача: https://leetcode.com/problems/valid-anagram/
Подсказки:
"""


class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram3(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        for char in s:
            if char in t:
                t.remove(char)
            else:
                return False
        if len(t) > 0:
            return False
        return True


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ("anagram",  "nagaram", True),
        ("rat",  "car", False),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.isAnagram(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {y=} -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')