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
    def inorderTraversal2(
            self, root: Optional[TreeNode]
    ) -> list[int]:
        """Решение задачи"""
        result = []

        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)  # Обходим левое поддерево
            result.append(node.val)  # Посещаем текущий узел
            inorder(node.right)  # Обходим правое поддерево

        inorder(root)
        return result

    def inorderTraversal(
            self, root: Optional[TreeNode]
    ) -> list[int]:
        """Решение задачи"""
        if not root:
            return []
        return self.inorderTraversal(root.left) + [
            root.val] + self.inorderTraversal(root.right)


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
        ([1,None,2,3], [1,3,2]),
        ([1,2,3,4,5,None,8,None,None,6,7,9], [4,2,6,5,7,1,3,9,8]),
        ([], []),
        ([1], [1]),
        ([2,4,5,None,None,6,7], [4, 2, 6, 5, 7]),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        root = build_tree(x)
        result = cls.inorderTraversal(root)
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')