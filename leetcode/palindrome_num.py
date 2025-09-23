"""
Задача: https://leetcode.com/problems/palindrome-number/
Подсказки:
"""

class Solution(object):
    def isPalindrome_old(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        return str(x) == str(x)[::-1]

    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10


if __name__=='__main__':
    cls = Solution()

    tests = [
        (121, True), (-121, False), (10, False), (0, True),
        (12321, True), (12345, False), (1001, True)
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.isPalindrome(x)
        status = "✓" if result == expected else "✗"
        print(f"Тест {i}: x={x} -> {result} (ожидается: {expected}) {status}")
        #assert result == expected, f"Тест {i} не пройден"

    print("Все тесты пройдены")