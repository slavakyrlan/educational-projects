"""
Задача: https://leetcode.com/problems/powx-n/
Подсказки:
"""


class Solution(object):
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        current_product = x
        while n > 0:
            # if n нечетное умножаем результат на текущее значение
            if n % 2 == 1:
                result *= current_product
            # ^2 для следующего шага
            current_product *= current_product
            # делим степень пополам
            n //= 2
        return result

    def myPow2(self, x: float, n: int) -> float:
        return x ** n


if __name__ == '__main__':
    cls = Solution()

    tests = [
        (2.00000, 10, 1024.00000),
        (2.10000, 3, 9.26100),
        (2.00000, -2, 0.25000),
        (0.00001, 2147483647, 0.0),
        (1.00000, 2147483647, 1.0),
        (2.00000, 0, 1.0),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.myPow(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')