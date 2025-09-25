"""
Задача: https://leetcode.com/problems/length-of-last-word/description/
Подсказки:
"""

class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        """Решение задачи"""
        last_word = s.split()[-1]
        return len(last_word)

if __name__=='__main__':
    cls = Solution()

    tests = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("Today is a nice day", 3),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.lengthOfLastWord(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')