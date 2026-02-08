from src.hash_map.longest_consecutive import longest_consecutive


def test_basic_sequence():
    """Test basic consecutive sequence"""
    nums = [100, 4, 200, 1, 3, 2]
    assert longest_consecutive(nums) == 4  # [1, 2, 3, 4]


def test_long_sequence():
    """Test longer consecutive sequence"""
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert longest_consecutive(nums) == 9  # [0, 1, 2, 3, 4, 5, 6, 7, 8]


def test_empty_list():
    """Test with empty list"""
    assert longest_consecutive([]) == 0


def test_single_element():
    """Test with single element"""
    assert longest_consecutive([1]) == 1


def test_no_consecutive():
    """Test when no numbers are consecutive"""
    nums = [1, 3, 5, 7, 9]
    assert longest_consecutive(nums) == 1


def test_all_consecutive():
    """Test when all numbers are consecutive"""
    nums = [1, 2, 3, 4, 5]
    assert longest_consecutive(nums) == 5


def test_duplicate_numbers():
    """Test with duplicate numbers"""
    nums = [1, 2, 0, 1, 2, 3]
    assert longest_consecutive(nums) == 4  # [0, 1, 2, 3]


def test_negative_numbers():
    """Test with negative numbers"""
    nums = [-1, -2, 0, 1, 2]
    assert longest_consecutive(nums) == 5  # [-2, -1, 0, 1, 2]


def test_unsorted_input():
    """Test with unsorted input"""
    nums = [9, 1, 4, 7, 3, 2, 8, 5, 6]
    assert longest_consecutive(nums) == 9  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_multiple_sequences():
    """Test with multiple separate sequences"""
    nums = [10, 5, 6, 11, 12, 1, 2]
    assert longest_consecutive(nums) == 3  # [10, 11, 12] or [5, 6, ...] consider the longer


def test_large_gaps():
    """Test with large gaps between numbers"""
    nums = [1, 1000, 2, 3, 1001, 1002]
    assert longest_consecutive(nums) == 3  # [1, 2, 3] or [1000, 1001, 1002]


def test_two_element_consecutive():
    """Test with two consecutive elements"""
    nums = [1, 2]
    assert longest_consecutive(nums) == 2


def test_two_element_non_consecutive():
    """Test with two non-consecutive elements"""
    nums = [1, 3]
    assert longest_consecutive(nums) == 1


def test_all_same_number():
    """Test with all same numbers"""
    nums = [1, 1, 1, 1]
    assert longest_consecutive(nums) == 1
