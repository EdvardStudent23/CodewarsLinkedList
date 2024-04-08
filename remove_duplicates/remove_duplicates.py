class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return None
    else:
        cur = head
        while cur:
            next_n = cur.next
            while next_n and next_n.data == cur.data:
                next_n = next_n.next
            cur.next, cur = next_n, next_n
        return head