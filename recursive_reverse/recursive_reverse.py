class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head == None or head.next == None:
        return head
    n_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return n_head