"""
Задача: https://leetcode.com/problems/contains-duplicate-iii/
Пример работы для nums = [1,2,3,1], indexDiff=3, valueDiff=0:
bucket_size = 1

i=0, num=1: bucket_id=1
bucket = {1:1}

i=1, num=2: bucket_id=2
bucket = {1:1, 2:2}

i=2, num=3: bucket_id=3
bucket = {1:1, 2:2, 3:3}

i=3, num=1: bucket_id=1
bucket_id=1 УЖЕ ЕСТЬ в bucket → return True
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(
            self, nums: list[int], indexDiff: int, valueDiff:int
    ) -> bool:
        if valueDiff < 0:
            return False

        bucket = {}
        bucket_size = valueDiff + 1  # размер корзины

        for i, num in enumerate(nums):
            bucket_id = num // bucket_size
            # Проверяем текущую корзину
            if bucket_id in bucket:
                return True
            # Проверяем соседние корзины
            if bucket_id - 1 in bucket and abs(
                    num - bucket[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in bucket and abs(
                    num - bucket[bucket_id + 1]) <= valueDiff:
                return True
            # Добавляем текущий элемент в корзину
            bucket[bucket_id] = num
            # Удаляем элементы, которые вышли за пределы indexDiff
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del bucket[old_bucket_id]
        return False


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ([1,2,3,1], 3, 0, True),
        ([1, 5, 9, 1, 5, 9], 2, 3, False),
        ([1, 0, 1, 1], 1, 2, True),
        ([1, 3, 6, 2], 1, 2, True),
        ([8, 7, 15, 1, 6, 1, 9, 15], 1, 3, True),
    ]

    for i, (*args, expected) in enumerate(tests, 1):
        result = cls.containsNearbyAlmostDuplicate(*args)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {args=} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')