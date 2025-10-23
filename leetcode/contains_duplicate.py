"""
Задача: https://leetcode.com/problems/contains-duplicate/
Подсказки:
"""


class Solution(object):
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.containsDuplicate(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')