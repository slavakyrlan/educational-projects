"""
Задача: https://leetcode.com/problems/longest-common-prefix/
Подсказки:
- startswith https://pythonz.net/references/named/str.startswith/
"""

class Solution(object):
    def longestCommonPrefix_old(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

if __name__=='__main__':
    cls = Solution()

    tests = [
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["a"], "a"),
        (["prefix", "preface", "premium"], "pre")
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.longestCommonPrefix(x)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')