from typing import Optional

from src.linked_list.reverse_list import reverse_list, ListNode


def list_to_array(head: Optional[ListNode]) -> list[int]:
    """Helper function to convert linked list to array for testing"""
    if head is None:
        return []

    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def array_to_list(arr: list[int]) -> ListNode:
    """Helper function to create linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def test_basic_reversal():
    """Test basic linked list reversal"""
    head = array_to_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    assert list_to_array(reversed_head) == [5, 4, 3, 2, 1]


def test_empty_list():
    """Test with empty list"""
    assert reverse_list(None) is None


def test_single_node():
    """Test with single node"""
    head = ListNode(1)
    reversed_head = reverse_list(head)
    assert reversed_head.val == 1
    assert reversed_head.next is None


def test_two_nodes():
    """Test with two nodes"""
    head = array_to_list([1, 2])
    reversed_head = reverse_list(head)
    assert list_to_array(reversed_head) == [2, 1]


def test_three_nodes():
    """Test with three nodes"""
    head = array_to_list([1, 2, 3])
    reversed_head = reverse_list(head)
    assert list_to_array(reversed_head) == [3, 2, 1]


def test_duplicate_values():
    """Test with duplicate values"""
    head = array_to_list([1, 1, 2, 3, 3])
    reversed_head = reverse_list(head)
    assert list_to_array(reversed_head) == [3, 3, 2, 1, 1]
