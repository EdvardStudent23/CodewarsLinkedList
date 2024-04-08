from preloaded import Node

def swap_pairs(head):
    if head == None or head.next == None:
        return head
    else:
        exam = Node()
        exam.next, prev = head, exam
    while prev.next and prev.next.next:
        one, second = prev.next, prev.next.next
        one.next, second.next = second.next, one
        prev.next = second
        prev = prev.next.next

    return exam.next