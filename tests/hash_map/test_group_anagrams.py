from src.hash_map.group_anagrams import group_anagrams

class TestGroupAnagrams:
    def test_basic_anagrams(self):
        """Test basic anagram grouping"""
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = group_anagrams(strs)
        
        # Convert to sets for easier comparison (order doesn't matter)
        result_sets = [set(group) for group in result]
        expected_sets = [{"eat", "tea", "ate"}, {"tan", "nat"}, {"bat"}]
        
        assert len(result) == 3
        assert all(expected in result_sets for expected in expected_sets)
    
    def test_empty_list(self):
        """Test with empty input"""
        assert group_anagrams([]) == []
    
    def test_single_string(self):
        """Test with single string"""
        result = group_anagrams(["a"])
        assert result == [["a"]]
    
    def test_no_anagrams(self):
        """Test when no strings are anagrams of each other"""
        strs = ["abc", "def", "ghi"]
        result = group_anagrams(strs)
        assert len(result) == 3
        assert all(len(group) == 1 for group in result)
    
    def test_all_anagrams(self):
        """Test when all strings are anagrams"""
        strs = ["abc", "bca", "cab"]
        result = group_anagrams(strs)
        assert len(result) == 1
        assert set(result[0]) == {"abc", "bca", "cab"}
    
    def test_empty_strings(self):
        """Test with empty strings"""
        strs = ["", "", "a"]
        result = group_anagrams(strs)
        result_sets = [set(group) for group in result]
        
        assert len(result) == 2
        assert set([""]) in result_sets or ["", ""] in result
