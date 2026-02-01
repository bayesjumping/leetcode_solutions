from typing import Optional

from .helpers import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list.
    
    Args:
        head: Head of the linked list to reverse
        
    Returns:
        Head of the reversed linked list
        
    Example:
        >>> # Input: 1 -> 2 -> 3 -> 4 -> 5
        >>> # Output: 5 -> 4 -> 3 -> 2 -> 1
    """
    prev: Optional[ListNode] = None
    curr = head
    
    while curr:
        # Save next before we overwrite it
        next_node = curr.next
        
        # Reverse the pointer
        curr.next = prev
        
        # Move pointers forward
        prev = curr
        curr = next_node
    
    # prev is now the new head
    return prev
