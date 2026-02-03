def has_cycle(head):
    """
    Detect if a linked list contains a cycle using Floyd's algorithm.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        bool: True if cycle exists, False otherwise
    """
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next          # Move slow by 1 step
        fast = fast.next.next     # Move fast by 2 steps
        
        if slow == fast:          # Pointers met - cycle detected!
            return True
    
    return False                  # Fast reached end - no cycle
