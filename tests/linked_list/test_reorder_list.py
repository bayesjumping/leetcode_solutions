from src.linked_list.helpers import array_to_list, list_to_array
from src.linked_list.has_cycle import has_cycle
from src.linked_list.reorder_list import reorder_list


def test_empty_list():
    head = array_to_list([])
    reorder_list(head)
    assert list_to_array(head) == []


def test_single_node():
    head = array_to_list([1])
    reorder_list(head)
    assert list_to_array(head) == [1]
    assert has_cycle(head) is False


def test_two_nodes_no_change():
    head = array_to_list([1, 2])
    reorder_list(head)
    assert list_to_array(head) == [1, 2]
    assert has_cycle(head) is False


def test_three_nodes():
    head = array_to_list([1, 2, 3])
    reorder_list(head)
    assert list_to_array(head) == [1, 3, 2]
    assert has_cycle(head) is False


def test_even_length():
    head = array_to_list([1, 2, 3, 4])
    reorder_list(head)
    assert list_to_array(head) == [1, 4, 2, 3]
    assert has_cycle(head) is False


def test_odd_length():
    head = array_to_list([1, 2, 3, 4, 5])
    reorder_list(head)
    assert list_to_array(head) == [1, 5, 2, 4, 3]
    assert has_cycle(head) is False


def test_duplicate_values():
    head = array_to_list([1, 1, 2, 2, 3, 3])
    reorder_list(head)
    assert list_to_array(head) == [1, 3, 1, 3, 2, 2]
    assert has_cycle(head) is False
