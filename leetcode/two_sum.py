"""
Задача: https://leetcode.com/problems/two-sum/description/
Подсказки: https://ru.hexlet.io/qna/python/questions/chto-delaet-metod-enumerate-python
"""

class Solution(object):
    def twoSum(self,
               nums: list[int],
               target: int
               )->list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


if __name__=='__main__':
    cls = Solution()

    # Тест 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = cls.twoSum(nums1, target1)
    print(f"Тест 1: nums={nums1}, target={target1} -> {result1}")
    assert result1 == [0, 1] or result1 == [1, 0], "Тест 1 не пройден"

    # Тест 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = cls.twoSum(nums2, target2)
    print(f"Тест 2: nums={nums2}, target={target2} -> {result2}")
    assert result2 == [1, 2] or result2 == [2, 1], "Тест 2 не пройден"

    # Тест 3
    nums3 = [3, 3]
    target3 = 6
    result3 = cls.twoSum(nums3, target3)
    print(f"Тест 3: nums={nums3}, target={target3} -> {result3}")
    assert result3 == [0, 1] or result3 == [1, 0], "Тест 3 не пройден"

    print("Все тесты пройдены успешно!")