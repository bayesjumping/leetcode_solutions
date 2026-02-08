from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Find the longest consecutive sequence in O(n) time.
    
    Given an unsorted array of integers, find the length of the longest 
    consecutive elements sequence. The algorithm must run in O(n) time.
    
    Args:
        nums: List of integers
        
    Returns:
        Length of the longest consecutive sequence
        
    Example:
        >>> longest_consecutive([100, 4, 200, 1, 3, 2])
        4  # The sequence is [1, 2, 3, 4]
        
        >>> longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        9  # The sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    # Convert to set for O(1) lookups
    num_set = set(nums)
    longest_streak = 0
    
    # Check each number
    for num in num_set:
        # Only start counting if this is a sequence start
        # (i.e., num - 1 is not in the set)
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            
            # Count consecutive numbers forward
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
            
            # Update maximum length
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak
