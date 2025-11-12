"""
Задача: https://leetcode.com/problems/maximum-product-of-three-numbers/
Подсказки:
"""


class Solution(object):
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        #  после сортировки либо слева макс отриц, либо справа макс
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[0] * nums[1] * nums[-1])


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ([1,2,3], 6),
        ([1,2,3,4], 24),
        ([-1,-2,-3], -6),
        ([-100,-2,1,2,3], 600),
        ([0,0,0,1,2,3], 6),
        ([-1,-2,-3,-4], -6),
        ([1,1,1,1], 1)
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.maximumProduct(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')