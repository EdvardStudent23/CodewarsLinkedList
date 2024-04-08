""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    n_node = Node(data)
    if head is None or head.data >= data:
        n_node.next = head
        return n_node

    cur = head
    while cur.next is not None and cur.next.data <= data:
        cur = cur.next
    
    n_node.next, cur.next = cur.next, n_node
    
    return head