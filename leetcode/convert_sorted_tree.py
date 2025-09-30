"""
Задача: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Подсказки:
"""
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(
            self, nums: list[int]
    ) -> Optional[TreeNode]:
        """Решение задачи"""
        def buildBST(left, right):
            if left > right:
                return None
            # Средний элемент становится корнем
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            # Рекурсивно строим левое и правое поддеревья
            node.left = buildBST(left, mid - 1)
            node.right = buildBST(mid + 1, right)
            return node

        return buildBST(0, len(nums) - 1)


def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    """Преобразует дерево в список (обход в ширину)"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Убираем лишние None в конце
    while result and result[-1] is None:
        result.pop()

    return result


def lists_are_equal(list1: list[Optional[int]],
                    list2: list[Optional[int]]) -> bool:
    """Сравнивает два списка, игнорируя разные представления сбалансированного BST"""
    while list1 and list1[-1] is None:
        list1.pop()
    while list2 and list2[-1] is None:
        list2.pop()
    return list1 == list2


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ([-10,-3,0,5,9], [0,-3,9,-10,None,5]),
        ([1,3], [3,1]),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result = cls.sortedArrayToBST(x)
        result_list = tree_to_list(result)

        status = "✓" if lists_are_equal(result_list, expected) else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result_list=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')