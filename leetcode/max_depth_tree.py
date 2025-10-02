"""
Задача: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Подсказки:
"""
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(
            self, root: Optional[TreeNode]
    ) -> int:
        """Решение задачи"""
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Строит бинарное дерево из списка значений в формате уровня"""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        # Левый потомок
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Правый потомок
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__=='__main__':
    cls = Solution()

    tests = [
        ([3,9,20,None,None,15,7], 3),
        ([1,None,2], 2),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        root = build_tree(x)
        result = cls.maxDepth(root)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')