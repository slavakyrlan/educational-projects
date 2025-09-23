"""
Задача: https://leetcode.com/problems/roman-to-integer/description/
Подсказки:
"""

class Solution(object):
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """


if __name__=='__main__':
    cls = Solution()

    tests = [
        ('III', 3), ('LVIII', 50), ('MCMXCIV', 1994)
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.romanToInt(x)
        status = "✓" if result == expected else "✗"
        print(
            f'Тест {i}: str="{x}" -> {result} (ожидается: {expected}) {status}')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')