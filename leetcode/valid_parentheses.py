"""
Задача: https://leetcode.com/problems/valid-parentheses/description/
Подсказки:
"""

class Solution(object):
    def isValid_old(self, s: str) -> bool:
        """Решение задачи"""
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in brackets.values():  # открывающая
                stack.append(char)
            elif char in brackets:  # закрывающая
                # Проверяем стек и соответствие скобок
                if not stack or stack.pop() != brackets[char]:
                    return False
        return len(stack) == 0

    def isValid(self, s: str) -> bool:
        """Решение задачи"""
        if len(s) % 2 != 0:
            return False

        stack = []
        brackets = {')': '(', '}': '{', ']': '['}
        for char in s:
            print(char)
            if char in brackets:
                print(char)
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0


if __name__=='__main__':
    cls = Solution()

    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.isValid(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')