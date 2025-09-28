"""
Задача: https://leetcode.com/problems/merge-sorted-array/
Подсказки:
"""

class Solution(object):
    def merge2(
            self, nums1: list[int], m: int, nums2: list[int], n: int
    ) -> None | list:
        """Решение задачи"""
        i = m - 1  # последний реальный элемент в nums1
        j = n - 1  # последний элемент в nums2
        k = m + n - 1  # последняя позиция в nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        print(nums1)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1

    def merge(
            self, nums1: list[int], m: int, nums2: list[int], n: int
    ) -> None | list:
        merged_all = sorted(nums1[:m] + nums2[:n])
        for i in range(len(merged_all)):
            nums1[i] = merged_all[i]
        return nums1

if __name__=='__main__':
    cls = Solution()

    tests = [
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        ([1],1,[],0,[1]),
        ([0],0,[1],1,[1])
    ]

    for i, (nums1, m, nums2, n, expected) in enumerate(tests, 1):
        result = cls.merge(nums1, m, nums2, n)
        status = "✓" if result == expected else "✗"
        print(
            f' {status} Тест {i}: '
            f'{nums1=} {m=} {nums2=} {n=} '
            f'-> {result=} (ожидается {expected})'
        )
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')