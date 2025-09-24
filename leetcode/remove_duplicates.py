"""
Задача: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Подсказки:
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """Решение задачи"""
        pred = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[pred]:
                pred += 1
                nums[pred] = nums[i]
        return pred+1


if __name__=='__main__':
    cls = Solution()

    tests = [
        ([1,1,2], 2), # [1,2,_]
        ([0,0,1,1,1,2,2,3,3,4], 5), #[0,1,2,3,4,_,_,_,_,_]
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.removeDuplicates(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')