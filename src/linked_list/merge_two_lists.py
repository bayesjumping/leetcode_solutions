from typing import Optional

from .helpers import ListNode


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted linked list.
    
    Args:
        list1: Head of the first sorted linked list
        list2: Head of the second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
        
    Example:
        >>> # Input: list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4
        >>> # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
    """
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    return dummy.next
