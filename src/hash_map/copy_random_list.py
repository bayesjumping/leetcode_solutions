from typing import Optional, Dict


class Node:
    """Definition for a Node with random pointer."""

    def __init__(self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None) -> None:
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    """
    Deep copy a linked list with random pointers.
    
    Args:
        head: Head of the linked list to copy
        
    Returns:
        Head of the copied linked list
        
    Example:
        >>> # Creates a deep copy of the linked list where each node
        >>> # has a next pointer and a random pointer to any node in the list
    """
    if not head:
        return None

    old_to_copy: Dict[Optional[Node], Optional[Node]] = {None: None}

    # First pass: create all nodes
    curr = head
    while curr:
        copy = Node(curr.val)
        old_to_copy[curr] = copy
        curr = curr.next
    
    # Second pass: assign next and random pointers
    curr = head
    while curr:
        copy = old_to_copy[curr]
        copy.next = old_to_copy[curr.next]
        copy.random = old_to_copy[curr.random]
        curr = curr.next
    
    return old_to_copy[head]