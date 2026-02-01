from src.linked_list.merge_two_lists import merge_two_lists
from src.linked_list.helpers import ListNode, list_to_array, array_to_list


def test_merge_basic():
    """Test merging two sorted lists"""
    list1 = array_to_list([1, 2, 4])
    list2 = array_to_list([1, 3, 4])
    merged = merge_two_lists(list1, list2)
    assert list_to_array(merged) == [1, 1, 2, 3, 4, 4]


def test_merge_empty_lists():
    """Test with both lists empty"""
    assert merge_two_lists(None, None) is None


def test_merge_one_empty():
    """Test with one list empty"""
    list1 = array_to_list([1, 2, 3])
    merged1 = merge_two_lists(list1, None)
    assert list_to_array(merged1) == [1, 2, 3]
    
    list2 = array_to_list([1, 2, 3])
    merged2 = merge_two_lists(None, list2)
    assert list_to_array(merged2) == [1, 2, 3]


def test_merge_different_lengths():
    """Test with lists of different lengths"""
    list1 = array_to_list([1, 3, 5, 7, 9])
    list2 = array_to_list([2, 4])
    merged = merge_two_lists(list1, list2)
    assert list_to_array(merged) == [1, 2, 3, 4, 5, 7, 9]


def test_merge_single_nodes():
    """Test with single node lists"""
    list1 = ListNode(1)
    list2 = ListNode(2)
    merged = merge_two_lists(list1, list2)
    assert list_to_array(merged) == [1, 2]
