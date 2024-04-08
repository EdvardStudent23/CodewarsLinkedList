def loop_size(node):
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return 0
    else:
        length = 1
        slow = slow.next
        while slow != fast:
            slow = slow.next
            length += 1

    return length