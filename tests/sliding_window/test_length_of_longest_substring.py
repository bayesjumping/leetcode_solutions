from src.sliding_window.length_of_longest_substring import length_of_longest_substring


def test_basic_case():
    """Test with repeating characters - 'abc' is the longest"""
    assert length_of_longest_substring("abcabcbb") == 3


def test_all_same_characters():
    """Test when all characters are the same"""
    assert length_of_longest_substring("bbbbb") == 1


def test_no_repeating_characters():
    """Test with some repeating characters - 'wke' or 'kew' is longest"""
    assert length_of_longest_substring("pwwkew") == 3


def test_empty_string():
    """Test with empty input"""
    assert length_of_longest_substring("") == 0


def test_single_character():
    """Test with single character"""
    assert length_of_longest_substring("a") == 1


def test_two_characters_different():
    """Test with two different characters"""
    assert length_of_longest_substring("ab") == 2


def test_two_characters_same():
    """Test with two same characters"""
    assert length_of_longest_substring("aa") == 1


def test_no_duplicates():
    """Test when entire string has no repeating characters"""
    assert length_of_longest_substring("abcdefg") == 7


def test_repeating_at_end():
    """Test when character repeats at the end"""
    assert length_of_longest_substring("abcda") == 4


def test_with_spaces():
    """Test with spaces and special characters"""
    assert length_of_longest_substring("a b c a") == 3


def test_numeric_strings():
    """Test with numeric characters as strings"""
    assert length_of_longest_substring("12321") == 3
