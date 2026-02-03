from src.linked_list.has_cycle import has_cycle
from src.linked_list.helpers import ListNode


def test_no_cycle_empty():
    """Test with empty list"""
    assert has_cycle(None) is False


def test_no_cycle_single_node():
    """Test with single node and no cycle"""
    node = ListNode(1)
    assert has_cycle(node) is False


def test_no_cycle_multiple_nodes():
    """Test with multiple nodes and no cycle"""
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    assert has_cycle(head) is False


def test_cycle_single_node():
    """Test with single node pointing to itself"""
    node = ListNode(1)
    node.next = node
    assert has_cycle(node) is True


def test_cycle_at_end():
    """Test with cycle at the end of list"""
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle back to node2
    
    assert has_cycle(head) is True


def test_cycle_at_head():
    """Test with cycle back to head"""
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    
    head.next = node2
    node2.next = node3
    node3.next = head  # Cycle back to head
    
    assert has_cycle(head) is True


def test_cycle_two_nodes():
    """Test with two nodes forming a cycle"""
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1  # Cycle between two nodes
    
    assert has_cycle(node1) is True
