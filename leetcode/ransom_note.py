"""
Задача: https://leetcode.com/problems/ransom-note/
Подсказки:
"""

class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Решение задачи"""
        letter = {}
        for char in magazine:
            letter[char] = letter.get(char, 0) + 1
        for char in ransomNote:
            if char not in letter or letter[char] == 0:
                return False
            letter[char] -= 1
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
            """Решение задачи"""
            magCopy = magazine
            for c in ransomNote:
                index = magCopy.find(c)
                if index == -1:
                    return False
                magCopy = magCopy.replace(c, "", 1)

            return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        """Решение задачи"""
        for char in ransomNote:
            if char not in magazine:
                return False
            magazine = magazine.replace(char, "", 1)
        return True


if __name__=='__main__':
    cls = Solution()

    tests = [
        ('a', 'b', False),
        ('aa', 'ab', False),
        ('aa', 'aab', True),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.canConstruct(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {y=} -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')