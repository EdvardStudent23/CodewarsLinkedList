from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if  index < 0 or node is None:
        raise ValueError("Invalid index or there is a wrong node in input")

    current_index = 0
    while node:
        if current_index == index:
            return node
        current_index += 1
        node = node.next

    raise ValueError("Index out of range")
