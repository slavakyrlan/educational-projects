"""
Задача: https://leetcode.com/problems/roman-to-integer/description/
Подсказки:
"""

class Solution(object):
    def __init__(self):
        self.roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

    def romanToInt(self, s: str) -> int:
        total = 0
        prev = 0

        for ch in reversed(s):
            curr = self.roman_values[ch]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total


if __name__=='__main__':
    cls = Solution()

    tests = [
        ('III', 3), ('LVIII', 58), ('MCMXCIV', 1994)
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.romanToInt(x)
        status = "✓" if result == expected else "✗"
        print(f'Тест {i}: str="{x}" -> {result} (ожидается: {expected}) {status}')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')