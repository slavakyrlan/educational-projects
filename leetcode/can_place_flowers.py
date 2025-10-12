"""
Задача: https://leetcode.com/problems/can-place-flowers/
Подсказки:
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        """Решение задачи"""
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == length - 1) or (
                            flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ([1,0,0,0,1], 1, True),
        ([1,0,0,0,1], 2, False),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.canPlaceFlowers(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {y=} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')