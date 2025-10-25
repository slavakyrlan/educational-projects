"""
Задача: https://leetcode.com/problems/top-k-frequent-elements/
Подсказки:
Комментарий:
вернуть до k эдементов самые повторяющие
"""


class Solution(object):
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        number = dict()
        for num in nums:
            number[num] = number.get(num, 0) + 1
        sorted_items = sorted(
            number.items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in sorted_items[:k]]

    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        import heapq
        from collections import defaultdict
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = [num for freq, num in heap]
        result.sort(key=lambda x: freq_map[x], reverse=True)
        return result

    def topKFrequent3(self, nums: list[int], k: int) -> list[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        top = sorted(dic, key=dic.get, reverse=True)[:k]
        return top


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ([1,1,1,2,2,3], 2, [1,2]),
        ([1], 1, [1]),
        ([1,2,1,2,1,2,3,1,3,2], 2, [1,2]),
    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        result = cls.topKFrequent(x, y)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: {x=} {y=} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')