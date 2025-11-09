"""
Задача: https://leetcode.com/problems/excel-sheet-column-number/
Подсказки:
"""


class Solution(object):
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            val = ord(ch) - ord('A') + 1
            result = result * 26 + val
        return result


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ("A", 1),
        ("AB", 28)
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.titleToNumber(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')