from collections import defaultdict
from typing import Iterable


def group_anagrams(strings: Iterable[str]) -> list[list[str]]:
    """
    Group anagrams together from a list of strings.
    
    Args:
        strings: Iterable of strings to group by anagrams
        
    Returns:
        List of grouped anagrams
        
    Example:
        >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    anagram_map = defaultdict(list)
    for word in strings:
        key = "".join(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())
