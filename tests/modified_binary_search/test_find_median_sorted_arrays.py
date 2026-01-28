from src.modified_binary_search.find_median_sorted_arrays import find_median_sorted_arrays


class TestFindMedianSortedArrays:
    def test_odd_total_length(self):
        """Test with odd total number of elements."""
        nums1 = [1, 3]
        nums2 = [2]
        assert find_median_sorted_arrays(nums1, nums2) == 2.0
    
    def test_even_total_length(self):
        """Test with even total number of elements."""
        nums1 = [1, 2]
        nums2 = [3, 4]
        assert find_median_sorted_arrays(nums1, nums2) == 2.5
    
    def test_empty_first_array(self):
        """Test when first array is empty."""
        nums1 = []
        nums2 = [1, 2, 3, 4, 5]
        assert find_median_sorted_arrays(nums1, nums2) == 3.0
    
    def test_empty_second_array(self):
        """Test when second array is empty."""
        nums1 = [1, 2, 3, 4, 5]
        nums2 = []
        assert find_median_sorted_arrays(nums1, nums2) == 3.0
    
    def test_single_element_each(self):
        """Test with single element in each array."""
        nums1 = [1]
        nums2 = [2]
        assert find_median_sorted_arrays(nums1, nums2) == 1.5
    
    def test_different_sizes(self):
        """Test with arrays of different sizes."""
        nums1 = [1, 3, 5, 7, 9]
        nums2 = [2, 4, 6]
        assert find_median_sorted_arrays(nums1, nums2) == 4.5
    
    def test_no_overlap(self):
        """Test when arrays have no overlapping values."""
        nums1 = [1, 2, 3]
        nums2 = [10, 11, 12]
        assert find_median_sorted_arrays(nums1, nums2) == 6.5
    
    def test_duplicate_values(self):
        """Test with duplicate values across arrays."""
        nums1 = [1, 2, 2]
        nums2 = [2, 3, 4]
        assert find_median_sorted_arrays(nums1, nums2) == 2.0
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums1 = [-5, -3, -1]
        nums2 = [-4, -2, 0]
        assert find_median_sorted_arrays(nums1, nums2) == -2.5
    
    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        nums1 = [-3, 0, 3]
        nums2 = [-2, 1, 4]
        assert find_median_sorted_arrays(nums1, nums2) == 0.5
