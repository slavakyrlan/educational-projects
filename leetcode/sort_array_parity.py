"""
Задача: https://leetcode.com/problems/sort-array-by-parity/
Подсказки:
"""


class Solution(object):
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        result_1 = []
        result_2 = []
        for num in nums:
            if num % 2 == 0:
                result_1.append(num)
            else:
                result_2.append(num)
        return result_1 + result_2

    def sortArrayByParity2(self, nums: list[int]) -> list[int]:
        evens = []
        odds = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        return evens + odds



if __name__ == '__main__':
    cls = Solution()

    tests = [
        ([3,1,2,4], [2,4,3,1]),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.sortArrayByParity(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')