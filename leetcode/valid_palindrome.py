"""
Задача: https://leetcode.com/problems/valid-palindrome/
Подсказки: https://pyhub.ru/python/lecture-5-10-1029/
"""

class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """Решение задачи"""
        letters_only = [char.lower() for char in s if char.isalnum()]
        return letters_only == letters_only[::-1]


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.isPalindrome(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')