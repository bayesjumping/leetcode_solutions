def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Uses a sliding window approach with a hash map to track character positions.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
        
    Example:
        >>> length_of_longest_substring("abcabcbb")
        3
        >>> length_of_longest_substring("bbbbb")
        1
    """
    char_index_map = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_index_map:
            left = max(char_index_map[char] + 1, left)
        
        char_index_map[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length
