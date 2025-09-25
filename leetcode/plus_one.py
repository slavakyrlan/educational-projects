"""
Задача: https://leetcode.com/problems/plus-one/description/
Подсказки:
- range start, end, step
"""

class Solution(object):
    def plusOne(self, digits: list[int]) -> list[int]:
        """Решение задачи. range(n)[::-1]"""
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits

    def plusOne_new(self, digits: list[int]) -> list[int]:
        """Решение задачи"""
        num = int(''.join(map(str, digits))) + 1
        return list(map(int, str(num)))



if __name__=='__main__':
    cls = Solution()

    tests = [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([9], [1,0]),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.plusOne(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')