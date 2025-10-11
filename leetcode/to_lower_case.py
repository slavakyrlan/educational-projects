"""
Задача: https://leetcode.com/problems/to-lower-case
Подсказки:
"""


class Solution(object):
    def toLowerCase(self,s: str) -> str:
        """Решение задачи"""
        return s.lower()


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ("Hello", "hello"),
        ("here", "here"),
        ("LOVELY", "lovely"),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.toLowerCase(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')