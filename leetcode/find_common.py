"""
Задача: https://leetcode.com/problems/find-common-characters/
Подсказки:
"""


class Solution(object):
    def commonChars(self, words: list[str]) -> list[str]:
        if not words:
            return []

        # 26 английских букв
        min_freq = [float('inf')] * 26

        for word in words:
            #  частоты для текущего слова
            curr_freq = [0] * 26
            for char in word:
                # преобразуем символ в индекс (a=0, b=1, ..., z=25)
                curr_freq[ord(char) - ord('a')] += 1

            # обновляем минимальные частоты
            for i in range(26):
                min_freq[i] = min(min_freq[i], curr_freq[i])

        result = []
        for i in range(26):
            # добавляем символ столько раз
            # сколько он встречается во всех словах
            result.extend([chr(ord('a') + i)] * min_freq[i])

        return result


if __name__ == '__main__':
    cls = Solution()

    tests = [
        (["bella","label","roller"], ["e","l","l"]),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.commonChars(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')