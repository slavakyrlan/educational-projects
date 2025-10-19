"""
Задача: https://leetcode.com/problems/keyboard-row/
Подсказки: https://docs-python.ru/tutorial/obschie-operatsii-mnozhestvami-set-frozenset-python/metod-sets-issubset/
"""


class Solution(object):
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            lower_word = word.lower()
            if set(lower_word).issubset(row1) or \
                    set(lower_word).issubset(row2) or \
                    set(lower_word).issubset(row3):
                result.append(word)
        return result

    def findWords2(self, words):
        result = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        for word in words:
            lower_word = set(word.lower())
            if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
                result.append(word)
        return result

    def findWords3(self, words: list[str]) -> list[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

        return [word for word in words
                if
                any(set(word.lower()).issubset(row) for row in rows)]


if __name__ == '__main__':
    cls = Solution()

    tests = [
        (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
        (["omk"], []),
        (["adsdf", "sfd"], ["adsdf", "sfd"]),
        (["a", "q", "z"], ["a", "q", "z"]),
        (["asdfghjklASDFGHJKL"], ["asdfghjklASDFGHJKL"]),
        (["qwertyuiopQWERTYUIOP"], ["qwertyuiopQWERTYUIOP"]),
        (["zxcvbnmZXCVBNM"], ["zxcvbnmZXCVBNM"]),
        (["mixed"], []),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.findWords2(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')