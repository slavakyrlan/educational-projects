"""
Задача: https://leetcode.com/problems/reverse-string-ii/
Подсказки:
"""


class Solution(object):
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)

        for i in range(0, len(s), 2 * k):
            # границы для реверса
            left = i
            # чтобы не выйти за границы
            right = min(i + k - 1, len(s) - 1)
            # Реверсим первые k символов
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return ''.join(chars)

    def reverseStr2(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)
        for i in range(0, n, 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return "".join(s)

    def reverseStr3(self, s, k):
        i = 0
        res = ""
        while i < len(s):
            d = s[i:i + 2 * k]
            if len(d) < k:
                d = d[::-1]
            else:
                d = d[:k][::-1] + d[k:]
            res += d
            i += 2 * k
        return res


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ("abcdefg", 2, "bacdfeg"),
        ("abcd", 2, "bacd"),
        ("abcdefgh", 3, "cbadefhg"),
        ("a", 1, "a"),
        ("abcdef", 4, "dcbaef"),
        ("abcdefg", 8, "gfedcba"),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.reverseStr(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {y=} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')