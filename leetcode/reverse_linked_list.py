"""
Задача: https://leetcode.com/problems/reverse-linked-list/
Подсказки:
- https://habr.com/ru/articles/833624/
- https://www.youtube.com/watch?v=ykY4pfKa7tU 141
- https://www.youtube.com/watch?v=gXg78QGgANs 206
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(
            self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_temp = current.next  # сохраняем следующий узел
            current.next = prev  # разворачиваем указатель
            prev = current  # двигаем prev вперед
            current = next_temp  # двигаем current вперед
        return prev

    def reverseList2(
            self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList2(head.next)
        # разворачиваем текущий указатель
        head.next.next = head
        head.next = None
        return new_head


def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == '__main__':
    cls = Solution()

    tests = [
        [1, 2, 3, 4, 5],
        [1, 2],
        []
    ]

    for i, tests in enumerate(tests, 1):
        head = list_to_linkedlist(tests)
        reversed_head = cls.reverseList(head)
        result = linkedlist_to_list(reversed_head)
        expected = tests[::-1]
        status = "✓" if result == expected else "✗"
        print(f' {status} Тест {i} -> {result=} (ожидается {expected})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')