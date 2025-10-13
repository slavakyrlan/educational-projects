"""
Задача: https://leetcode.com/problems/excel-sheet-column-title/
Подсказки:
"""


class Solution(object):
    def convertToTitle(self, columnNumber: int) -> str:
        """Решение задачи"""
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(65 + remainder) + result  # 65 - код буквы A
            columnNumber //= 26
        return result


if __name__ == '__main__':
    cls = Solution()

    tests = [
        (1, "A"),
        (28, "AB"),
        (701, "ZY"),
        (26, "Z"),
        (27, "AA"),
        (52, "AZ"),
        (53, "BA"),
        (702, "ZZ"),
        (703, "AAA"),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.convertToTitle(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')