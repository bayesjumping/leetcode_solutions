from typing import Optional

from .helpers import ListNode


def reorder_list(head: Optional[ListNode]) -> None:
    """Reorder list by splitting, reversing second half, and merging alternately.

    Reorders in-place to: L0 → Ln → L1 → Ln-1 → L2 → ...
    """
    if head is None or head.next is None:
        return

    # Step 1: Find middle using fast/slow pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next

    # Step 2: Reverse second half in-place
    second = slow.next  # type: ignore[assignment]
    prev: Optional[ListNode] = None
    slow.next = None  # Break connection
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # Step 3: Merge alternately
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
