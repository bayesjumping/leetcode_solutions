from src.linked_list.add_two_numbers import add_two_numbers
from src.linked_list.helpers import list_to_array, array_to_list


def test_example_case():
    """Test the canonical example: 342 + 465 = 807"""
    l1 = array_to_list([2, 4, 3])
    l2 = array_to_list([5, 6, 4])
    result = add_two_numbers(l1, l2)
    assert list_to_array(result) == [7, 0, 8]


def test_with_carry():
    """Test addition that produces a carry: 99 + 1 = 100"""
    l1 = array_to_list([9, 9])
    l2 = array_to_list([1])
    result = add_two_numbers(l1, l2)
    assert list_to_array(result) == [0, 0, 1]


def test_all_nines_carry():
    """Test 999 + 1 = 1000"""
    l1 = array_to_list([9, 9, 9])
    l2 = array_to_list([1])
    result = add_two_numbers(l1, l2)
    assert list_to_array(result) == [0, 0, 0, 1]


def test_single_digits_no_carry():
    """Test 3 + 4 = 7"""
    l1 = array_to_list([3])
    l2 = array_to_list([4])
    result = add_two_numbers(l1, l2)
    assert list_to_array(result) == [7]


def test_single_digits_with_carry():
    """Test 7 + 8 = 15"""
    l1 = array_to_list([7])
    l2 = array_to_list([8])
    result = add_two_numbers(l1, l2)
    assert list_to_array(result) == [5, 1]


def test_different_lengths():
    """Test lists of different lengths: 5 + 123 = 128"""
    l1 = array_to_list([5])
    l2 = array_to_list([3, 2, 1])
    result = add_two_numbers(l1, l2)
    assert list_to_array(result) == [8, 2, 1]


def test_zeros():
    """Test 0 + 0 = 0"""
    l1 = array_to_list([0])
    l2 = array_to_list([0])
    result = add_two_numbers(l1, l2)
    assert list_to_array(result) == [0]
