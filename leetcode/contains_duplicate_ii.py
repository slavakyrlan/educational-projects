"""
Задача: https://leetcode.com/problems/contains-duplicate-ii/
Подсказки:
"""


class Solution(object):
    def containsNearbyDuplicate(
            self, nums: list[int], k: int
    ) -> bool:
        len_ = len(nums)
        for i in range(len_):
            # начинаем с i+1 чтобы избежать i == j
            for j in range(i+1, len_):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ([1,2,3,1], 3, True),
        ([1,0,1,1], 1, True),
        ([1,2,3,1,2,3], 2, False),
    ]

    for i, (*args, expected) in enumerate(tests, 1):
        result = cls.containsNearbyDuplicate(*args)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {args=} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')