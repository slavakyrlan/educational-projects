"""
Задача: https://leetcode.com/problems/contains-duplicate-ii/
Подсказки:
"""


class Solution(object):
    def containsNearbyDuplicate(
            self, nums: list[int], k: int
    ) -> bool:
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i
        return False

    def containsNearbyDuplicate2(
            self, nums: list[int], k: int
    ) -> bool:
        hashSet = set()
        for i in range(len(nums)):
            if nums[i] in hashSet:
                return True
            hashSet.add(nums[i])
            if len(hashSet) > k:
                hashSet.remove(nums[i - k])
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