"""
Задача: https://leetcode.com/problems/longest-palindrome/
Подсказки:
"""


class Solution(object):
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        char_count = Counter(s)

        length = 0
        has_odd = False

        for count in char_count.values():
            if count % 2 == 0:
                # четные частоты полностью идут в палиндром
                length += count
            else:
                # нечетные частоты: берем count-1 (делаем четным)
                length += count - 1
                has_odd = True
        # если был хоть один нечетный символ можно поставить один в центр
        if has_odd:
            length += 1
        return length

    def longestPalindrome2(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        odds = sum(1 for v in count.values() if v % 2)
        return len(s) - odds + (1 if odds else 0)

    def longestPalindrome3(self, s: str) -> int:
        count = {}
        for chars in s:
            count[chars] = count.get(chars, 0) + 1
        single = 0
        ans = 0
        for i in count:
            if count[i] % 2 == 0:
                ans += count[i]
            else:
                ans += count[i] - 1
                single = 1

        return ans + single


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ("abccccdd", 7),
        ("a", 1),
        ("aaabbbcc", 7),
        ("abc", 1),
        ("aabb", 4),
        ("", 0),
        ("aaa", 3),
        ("aabbcc", 6)
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.longestPalindrome(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')
