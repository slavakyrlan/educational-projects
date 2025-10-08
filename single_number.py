"""
Задача: https://leetcode.com/problems/single-number/
Подсказки:
"""


class Solution(object):
    def singleNumber(self, nums: list[int]) -> int:
        """Решение задачи"""


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ([2,2,1], 1),
        ([4,1,2,1,2], 4),
        ([1], 1),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.singleNumber(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')