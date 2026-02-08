from src.linked_list.remove_nth_from_end import remove_nth_from_end
from src.linked_list.helpers import ListNode, list_to_array, array_to_list


def test_remove_second_from_end():
    """Test removing second node from end"""
    head = array_to_list([1, 2, 3, 4, 5])
    result = remove_nth_from_end(head, 2)
    assert list_to_array(result) == [1, 2, 3, 5]


def test_remove_first_from_end():
    """Test removing last node"""
    head = array_to_list([1, 2, 3, 4, 5])
    result = remove_nth_from_end(head, 1)
    assert list_to_array(result) == [1, 2, 3, 4]


def test_remove_from_single_node():
    """Test with single node list"""
    head = ListNode(1)
    result = remove_nth_from_end(head, 1)
    assert result is None


def test_remove_from_two_nodes_first():
    """Test removing first node from two-node list"""
    head = array_to_list([1, 2])
    result = remove_nth_from_end(head, 2)
    assert list_to_array(result) == [2]


def test_remove_from_two_nodes_second():
    """Test removing second node from two-node list"""
    head = array_to_list([1, 2])
    result = remove_nth_from_end(head, 1)
    assert list_to_array(result) == [1]


def test_remove_head():
    """Test removing the head node"""
    head = array_to_list([1, 2, 3, 4, 5])
    result = remove_nth_from_end(head, 5)
    assert list_to_array(result) == [2, 3, 4, 5]


def test_remove_middle():
    """Test removing a middle node"""
    head = array_to_list([1, 2, 3, 4, 5])
    result = remove_nth_from_end(head, 3)
    assert list_to_array(result) == [1, 2, 4, 5]


def test_with_duplicate_values():
    """Test with duplicate values in list"""
    head = array_to_list([1, 1, 1, 1])
    result = remove_nth_from_end(head, 2)
    assert list_to_array(result) == [1, 1, 1]


def test_remove_from_three_nodes():
    """Test with three-node list"""
    head = array_to_list([1, 2, 3])
    result = remove_nth_from_end(head, 2)
    assert list_to_array(result) == [1, 3]


def test_long_list():
    """Test with longer list"""
    head = array_to_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = remove_nth_from_end(head, 5)
    assert list_to_array(result) == [1, 2, 3, 4, 5, 7, 8, 9, 10]
