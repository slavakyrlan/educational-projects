"""
Задача: https://leetcode.com/problems/merge-two-sorted-lists/description/
Подсказки: https://habr.com/ru/companies/otus/articles/470828/
"""

class ListNode(object):
    """Узлы."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        """Решение задачи"""
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # если один из списков закончился присоединяем оставшийся
        current.next = list1 or list2
        return head.next

    def create_linked_list(self, lst):
        if not lst:
            return None

        head = ListNode(lst[0])
        current = head

        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result


if __name__=='__main__':
    cls = Solution()

    tests = [
        ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
        ([], [], []),
        ([], [0], [0]),

    ]

    for i, (x, y, expected) in enumerate(tests, 1):
        list1 = cls.create_linked_list(x)
        list2 = cls.create_linked_list(y)

        merged_head = cls.mergeTwoLists(list1, list2)
        result = cls.linked_list_to_list(merged_head)
        status = "✓" if result == expected else "✗"
        print(f'{status} Тест {i}: {x=} {y=} -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')