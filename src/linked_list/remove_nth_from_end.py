from typing import Optional

from .helpers import ListNode


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove the nth node from the end of a linked list.
    
    Uses the two-pointer technique where the right pointer moves n steps ahead first,
    then both pointers move together until right reaches the end. At that point, left
    is positioned just before the node to remove.
    
    Args:
        head: Head of the linked list
        n: Position from the end (1-indexed)
        
    Returns:
        Head of the modified linked list
        
    Example:
        >>> # Input: 1 -> 2 -> 3 -> 4 -> 5, n = 2
        >>> # Output: 1 -> 2 -> 3 -> 5
        
    Time Complexity: O(L) where L is the length of the list
    Space Complexity: O(1)
    """
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # Move right pointer n steps ahead
    while n > 0 and right:
        right = right.next
        n -= 1
    
    # Move both pointers until right reaches the end
    while right:
        left = left.next
        right = right.next
    
    # Remove the nth node from end
    left.next = left.next.next
    return dummy.next
