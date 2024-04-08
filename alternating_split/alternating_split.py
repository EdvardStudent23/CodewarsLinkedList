class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError('Your list should have 2 or more nodes')
    else:
        first_head, second_head = head, head.next
        first_cur, second_cur = first_head, second_head

    while second_cur != None and first_cur != None:
        first_cur.next = second_cur.next
        if first_cur.next is None:
            second_cur.next = None
        else:
            second_cur.next = first_cur.next.next
        first_cur, second_cur = first_cur.next, second_cur.next
    
    return Context(first_head, second_head)