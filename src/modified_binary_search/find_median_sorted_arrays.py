def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two sorted arrays in O(log min(m,n)) time.
    
    Strategy: Binary search on the partition position in the smaller array.
    A valid partition has all left elements <= all right elements.
    """
    a, b = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    # Ensure a is the smaller array
    if len(b) < len(a):
        a, b = b, a
    
    left, right = 0, len(a) - 1
    
    while True:
        # Partition indices
        partition_a = (left + right) // 2  # a partition
        partition_b = half - partition_a - 2  # b partition (to get half elements on left)

        # Get boundary elements (use infinity for out-of-bounds)
        a_left = a[partition_a] if partition_a >= 0 else float("-infinity")
        a_right = a[partition_a + 1] if (partition_a + 1) < len(a) else float("infinity")
        b_left = b[partition_b] if partition_b >= 0 else float("-infinity")
        b_right = b[partition_b + 1] if (partition_b + 1) < len(b) else float("infinity")

        # Check if partition is valid
        if a_left <= b_right and b_left <= a_right:
            # Correct partition found!
            if total % 2:  # Odd total length
                return min(a_right, b_right)
            else:  # Even total length
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            # Too many elements from a, search left
            right = partition_a - 1
        else:
            # Too few elements from a, search right
            left = partition_a + 1
