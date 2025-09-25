"""
Задача: https://leetcode.com/problems/remove-element/
Подсказки:
"""

class Solution(object):
    def removeElement_old(self, nums: list[int], val: int) -> int:
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k

    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        k = len(nums)
        return k


if __name__=='__main__':
    cls = Solution()

    tests = [
        ([3,2,2,3], 3, 2),
        ([0,1,2,2,3,0,4,2], 2, 5),
    ]

    for i, (x, val, expected) in enumerate(tests, 1):
        result = cls.removeElement(x,val)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {val=} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')