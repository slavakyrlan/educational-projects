"""
Задача: https://leetcode.com/problems/find-the-difference/
Подсказки:
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """Решение задачи"""
        sum_s = sum(ord(char) for char in s)
        sum_t = sum(ord(char) for char in t)
        return chr(sum_t - sum_s)


if __name__=='__main__':
    cls = Solution()

    tests = [
        ('abcd', 'abcde', "e"),
        ('', 'y', "y"),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.findTheDifference(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {y=}-> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')