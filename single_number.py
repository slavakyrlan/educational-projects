"""
Задача: https://leetcode.com/problems/single-number/
Подсказки:
- https://javarush.com/groups/posts/operator-xor-v-python
- https://www.youtube.com/watch?v=myW_9B9T_II
"""


class Solution(object):
    def singleNumber(self, nums: list[int]) -> int:
        """Решение задачи"""
        numer = {}
        for i in nums:
            numer[i] = numer.get(i, 0) + 1
        for num, count in numer.items():
            if count == 1:
                return num

    def singleNumber2(self, nums: list[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber3(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


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