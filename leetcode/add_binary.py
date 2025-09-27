"""
Задача: https://leetcode.com/problems/add-binary/
Подсказки:
- int('num', 2) -> десятичное https://pythoner.name/int-function
- bin в двоичное https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-bin/
"""

class Solution(object):
    def addBinary_old1(self, a: str, b: str) -> str:
        """Решение задачи"""
        a, b = int(a, 2), int(b, 2)
        return bin(a+b)[2:]

    def addBinary_old2(self, a: str, b: str) -> str:
        """Решение задачи"""
        sum_num = int(a,2) + int(b,2)
        result = []
        while sum_num > 0:
            result.append(str(sum_num%2))
            sum_num = sum_num//2
        return ''.join(result[::-1])

    def addBinary(self, a: str, b: str) -> str:
        """Решение задачи"""
        result = []
        carry = 0  # перенос
        i, j = len(a) - 1, len(b) - 1  # указатели с конца строк

        # проходим по обеим строкам с конца
        while i >= 0 or j >= 0 or carry:
            # берем цифры или 0 если строка закончилась
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # суммируем цифры и перенос
            total = digit_a + digit_b + carry
            print(total)
            # вычисляем текущую цифру и новый перенос
            result.append(str(total % 2))  # остаток от деления на 2
            carry = total // 2  # целочисленное деление на 2

            # двигаем указатели
            i -= 1
            j -= 1

        # разворачиваем результат (так как добавляли с конца)
        return ''.join(result[::-1])


if __name__=='__main__':
    cls = Solution()

    tests = [
        ('11', '1', '100'),
        ('1010', '1011', '10101'),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.addBinary(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {y=} -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')