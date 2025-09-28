"""
Задача: https://leetcode.com/problems/sqrtx/
Подсказки:
"""

class Solution(object):
    def mySqrt(self, x: int) -> int:
        """Решение задачи"""
        import math
        return int(math.sqrt(x))

    def mySqrt2(self, x: int) -> int:
        """Решение задачи"""
        return int(x**0.5)

    def mySqrt3(self, x: int) -> int:
        """Решение задачи"""
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            print('mid', mid)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
                print('l', left)
            else:
                right = mid - 1
                print('r', right)
        return right


if __name__=='__main__':
    cls = Solution()

    tests = [
        (4, 2),
        (8, 2),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.mySqrt3(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')