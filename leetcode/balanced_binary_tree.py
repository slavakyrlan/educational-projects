"""
Задача: https://leetcode.com/problems/balanced-binary-tree/
Подсказки:
"""
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(
            self, root: Optional[TreeNode]
    ) -> bool:
        def check_balance(node):
            """
            Возвращает (height, is_balanced)
            height - высота поддерева
            is_balanced - сбалансировано ли поддерево
            """
            if not node:
                return 0, True

            # Рекурсивно проверяем левое и правое поддеревья
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)

            # Текущее дерево сбалансировано, если:
            # 1. Левое и правое поддеревья сбалансированы
            # 2. Разница высот <= 1
            current_balanced = (left_balanced and right_balanced and
                                abs(left_height - right_height) <= 1)

            # Высота текущего узла = 1 + максимальная высота из поддеревьев
            current_height = 1 + max(left_height, right_height)

            return current_height, current_balanced

        _, is_balanced = check_balance(root)
        return is_balanced



def build_tree(values):
    """Строит дерево из списка значений (обход в ширину)"""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == '__main__':
    cls = Solution()

    tests = [
        ([3,9,20,None,None,15,7], True),
        ([1,2,2,3,3,None,None,4,4], False),
        ([],True),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        result_list = build_tree(x)
        result = cls.isBalanced(result_list)
        #result_list = isBalanced(x)

        status = "✓" if result==expected else "✗"
        print(f' {status} Тест {i}: strs="{x}" -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')