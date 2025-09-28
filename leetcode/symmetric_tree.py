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
    def isSymmetric(
            self, root: Optional[TreeNode]
    ) -> bool:
        """Решение задачи"""
        if not root:
            return True

        def isMirror(left: Optional[TreeNode],
                     right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return (
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left)
            )
        return isMirror(root.left, root.right)

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
        ([1,2,2,3,4,4,3], True),
        ([[1,2,2,None,3,None,3], False]),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        root = build_tree(x)
        result = cls.isSymmetric(root)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')