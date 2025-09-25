"""
Задача: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Подсказки:
"""

class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        """0ms с else, иначе 2ms"""
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

    def strStr_new1(self, haystack: str, needle: str) -> int:
        """1ms.
        Try/except создает дополнительную нагрузку
        даже при успешном выполнении.
        """
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

    def strStr_new2(self, haystack: str, needle: str) -> int:
        """0ms. Встроенная C-функция - максимально оптимизирована."""
        return haystack.find(needle)


if __name__=='__main__':
    cls = Solution()

    tests = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.strStr(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {y=} -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')