"""
Задача: https://leetcode.com/problems/climbing-stairs/description/
Подсказки:
"""


class Solution(object):
    def climbStairs(self, n: int) -> int:
        """Решение задачи"""
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__=='__main__':
    cls = Solution()

    tests = [
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.climbStairs(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: n="{x}" -> {result} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')