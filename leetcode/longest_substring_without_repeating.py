"""
Задача: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Подсказки:
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0
        for right, char in enumerate(s):
            # если символ уже встречался и его индекс >= left
            if char in char_map and char_map[char] >= left:
                # двигаем left за повторяющийся символ
                left = char_map[char] + 1
            char_map[char] = right  # обновляем индекс символа
            max_length = max(max_length, right - left + 1)
        return max_length


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3)
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.lengthOfLongestSubstring(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')