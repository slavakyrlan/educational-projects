"""
Задача:
Подсказки:
"""

class Solution(object):
    def example(self, *args, **kwargs):
        """Решение задачи"""



if __name__=='__main__':
    cls = Solution()

    tests = [
        ('x', 'y'),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.example(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')