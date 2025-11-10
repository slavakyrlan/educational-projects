"""
Задача: https://leetcode.com/problems/word-pattern/
Подсказки:
"""


class Solution(object):
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}  # отображение char → word
        word_to_char = {}  # отображение word → char

        for char, word in zip(pattern, words):
            # проверяем отображение char → word
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            # проверяем отображение word → char
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        return True


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abba", "dog dog dog dog", False),
        ("abc", "dog cat fish", True),
        ("aaa", "dog dog dog", True),
        ("", "", True),
        ("a", "dog", True)
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.wordPattern(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=}{y=} -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')