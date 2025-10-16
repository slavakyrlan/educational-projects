"""
Задача: https://leetcode.com/problems/reverse-words-in-a-string-iii/
Подсказки:
"""


class Solution(object):
    def reverseWords(self, s: str) -> str:
        """Решение задачи"""
        s = s[::-1].split()
        return ' '.join(s[::-1])

    def reverseWords2(self, s: str) -> str:
        """Решение задачи"""
        return ' '.join([z[::-1] for z in s.split(' ')])


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("Mr Ding", "rM gniD"),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.reverseWords(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')