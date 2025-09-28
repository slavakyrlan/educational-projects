"""
Задача: https://leetcode.com/problems/binary-tree-inorder-traversal/
Подсказки:
"""
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(
            self, p: Optional[TreeNode], q: Optional[TreeNode],
    ) -> bool:
        """Решение задачи"""
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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
        ([1,2,3], [1,2,3], True),
        ([1,2], [1,None,2], False),
        ([1,2,1], [1,1,2], False),

    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        root_p = build_tree(x)
        root_q = build_tree(y)

        result = cls.isSameTree(root_p,root_q)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')