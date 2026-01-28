def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two sorted arrays in O(log min(m,n)) time.
    
    Strategy: Binary search on the partition position in the smaller array.
    A valid partition has all left elements <= all right elements.
    """
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    # Ensure A is the smaller array
    if len(B) < len(A):
        A, B = B, A
    
    l, r = 0, len(A) - 1
    
    while True:
        # Partition indices
        i = (l + r) // 2  # A partition
        j = half - i - 2  # B partition (to get half elements on left)

        # Get boundary elements (use infinity for out-of-bounds)
        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # Check if partition is valid
        if Aleft <= Bright and Bleft <= Aright:
            # Correct partition found!
            if total % 2:  # Odd total length
                return min(Aright, Bright)
            else:  # Even total length
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            # Too many elements from A, search left
            r = i - 1
        else:
            # Too few elements from A, search right
            l = i + 1
