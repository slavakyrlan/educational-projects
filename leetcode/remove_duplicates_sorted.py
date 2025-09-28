"""
Задача: https://leetcode.com/problems/merge-two-sorted-lists/description/
Подсказки: https://habr.com/ru/companies/otus/articles/470828/
"""
from typing import Optional


class ListNode(object):
    """Узлы."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(
            self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Решение задачи"""
        current = head
        while current and current.next:
            if current.val == current.next.val:
                # пропускаем дубликат
                current.next = current.next.next
            else:
                current = current.next
        return head


def list_to_linkedlist(lst):
    """Преобразует список в связный список"""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    """Преобразует связный список в обычный список"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result



if __name__=='__main__':
    cls = Solution()

    tests = [
        ([1, 2, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([1, 1, 1], [1]),
    ]

    for i, (x, expected) in enumerate(tests, 1):
        # Преобразуем входной список в связный список
        head = list_to_linkedlist(x)
        # Удаляем дубликаты
        result_head = cls.deleteDuplicates(head)
        # Преобразуем результат обратно в список
        result = linkedlist_to_list(result_head)
        status = "✓" if result == expected else "✗"
        print(f'{status} Тест {i}: {x=} -> {result=} (ожидается {expected=})')
        # assert result == expected, f"Тест {i} не пройден"

    print('Все тесты пройдены')