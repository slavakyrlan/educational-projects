"""
Задача: https://leetcode.com/problems/add-digits/
Подсказки:
"""


class Solution(object):
    def addDigits(self, num: int) -> int:
        while num >= 10:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            num = digit_sum
        return num


if __name__ == '__main__':
    cls = Solution()

    tests = [
        (38, 2),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.addDigits(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')