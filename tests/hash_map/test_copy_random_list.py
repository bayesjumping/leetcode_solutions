from typing import Optional, Dict, List
from src.hash_map.copy_random_list import copy_random_list, Node


def create_random_list(values: List[int], random_indices: List[Optional[int]]) -> Optional[Node]:
    """
    Helper function to create a linked list with random pointers.
    
    Args:
        values: List of values for the nodes
        random_indices: List where random_indices[i] is the index of the node that 
                       nodes[i].random should point to (or None for null)
    
    Returns:
        Head of the created linked list
    """
    if not values:
        return None
    
    # Create all nodes first
    nodes = [Node(val) for val in values]
    
    # Set next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Set random pointers
    for i, random_idx in enumerate(random_indices):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]
    
    return nodes[0]


def verify_random_list_copy(original: Optional[Node], copied: Optional[Node]) -> bool:
    """
    Verify that the copied list is a deep copy of the original.
    
    Args:
        original: Head of the original linked list
        copied: Head of the copied linked list
        
    Returns:
        True if the copy is correct, False otherwise
    """
    if not original and not copied:
        return True
    
    if not original or not copied:
        return False
    
    # Build mapping from original nodes to their positions
    original_to_index: Dict[Node, int] = {}
    copied_nodes: List[Node] = []
    
    curr_orig, curr_copy = original, copied
    index = 0
    
    # First pass: collect all nodes and build index mapping
    while curr_orig and curr_copy:
        # Check that values match
        if curr_orig.val != curr_copy.val:
            return False
        
        # Check that nodes are different objects (deep copy)
        if curr_orig is curr_copy:
            return False
        
        original_to_index[curr_orig] = index
        copied_nodes.append(curr_copy)
        
        curr_orig = curr_orig.next
        curr_copy = curr_copy.next
        index += 1
    
    # Check that both lists ended at the same time
    if curr_orig is not None or curr_copy is not None:
        return False
    
    # Second pass: verify random pointers
    curr_orig, curr_copy = original, copied
    index = 0
    
    while curr_orig and curr_copy:
        if curr_orig.random is None:
            if curr_copy.random is not None:
                return False
        else:
            random_index = original_to_index[curr_orig.random]
            if curr_copy.random is not copied_nodes[random_index]:
                return False
        
        curr_orig = curr_orig.next
        curr_copy = curr_copy.next
        index += 1
    
    return True


def test_empty_list():
    """Test with empty list"""
    assert copy_random_list(None) is None


def test_single_node_no_random():
    """Test with single node and no random pointer"""
    head = Node(1)
    copied = copy_random_list(head)
    
    assert copied is not None
    assert copied.val == 1
    assert copied.next is None
    assert copied.random is None
    assert copied is not head  # Different object


def test_single_node_self_random():
    """Test with single node pointing to itself"""
    head = Node(1)
    head.random = head
    
    copied = copy_random_list(head)
    
    assert copied is not None
    assert copied.val == 1
    assert copied.next is None
    assert copied.random is copied  # Points to itself
    assert copied is not head  # Different object


def test_two_nodes_no_random():
    """Test with two nodes and no random pointers"""
    original = create_random_list([1, 2], [None, None])
    copied = copy_random_list(original)
    
    assert verify_random_list_copy(original, copied)


def test_two_nodes_with_random():
    """Test with two nodes where each points to the other"""
    original = create_random_list([1, 2], [1, 0])
    copied = copy_random_list(original)
    
    assert verify_random_list_copy(original, copied)


def test_complex_list():
    """Test with a more complex list structure"""
    # List: [7, 13, 11, 10, 1]
    # Random pointers: [null, 0, 4, 2, 0]
    original = create_random_list([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copied = copy_random_list(original)
    
    assert verify_random_list_copy(original, copied)


def test_all_nodes_point_to_head():
    """Test where all random pointers point to the head"""
    original = create_random_list([1, 2, 3, 4], [0, 0, 0, 0])
    copied = copy_random_list(original)
    
    assert verify_random_list_copy(original, copied)