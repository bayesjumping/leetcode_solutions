from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group anagrams together from a list of strings.
    
    Args:
        strs: List of strings to group by anagrams
        
    Returns:
        List of grouped anagrams
        
    Example:
        >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    anagram_map = defaultdict(list)
    for s in strs:
        sorted_s = "".join(sorted(s))
        anagram_map[sorted_s].append(s)
    return list(anagram_map.values())
