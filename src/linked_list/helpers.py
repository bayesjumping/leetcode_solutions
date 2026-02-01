from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def list_to_array(head: Optional[ListNode]) -> list[int]:
    """Helper function to convert linked list to array for testing."""
    if head is None:
        return []

    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def array_to_list(arr: list[int]) -> Optional[ListNode]:
    """Helper function to create linked list from array."""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head
