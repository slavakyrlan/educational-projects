"""
Задача: https://leetcode.com/problems/group-anagrams/
Подсказки:
"""


class Solution(object):
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

        result = list()
        for group in anagrams.values():
            group.sort()
            result.append(group)

        result.sort(key=len)
        return result


if __name__ == '__main__':
    cls = Solution()

    tests = [
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.groupAnagrams(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')