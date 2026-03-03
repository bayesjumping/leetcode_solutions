from .helpers import ListNode


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Add two numbers represented as reversed linked lists.

    Each node contains a single digit. The digits are stored in reverse order,
    such that the 1's digit is at the head of the list.

    Args:
        l1: Head of the first linked list
        l2: Head of the second linked list

    Returns:
        Head of a linked list representing the sum

    Example:
        >>> # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        >>> # Output: 7 -> 0 -> 8  (342 + 465 = 807)
    """
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        curr.next = ListNode(val)

        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next
