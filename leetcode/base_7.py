"""
Задача:
Подсказки:
"""

class Solution(object):
    def convertToBase7(self, num: int) -> str:
        """Решение задачи"""
        if num == 0:
            return '0'
        n = abs(num)
        result_rev = []
        while n > 0:
            result_rev.append(str(n % 7))
            n = n // 7
        base7_str = ''.join(result_rev[::-1])
        return base7_str if num >= 0 else '-' + base7_str


if __name__=='__main__':
    cls = Solution()

    tests = [
        (100, '202'),
        (-7, '-10')
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.convertToBase7(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')
