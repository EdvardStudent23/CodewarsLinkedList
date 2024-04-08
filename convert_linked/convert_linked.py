def stringify(node):
    if node is None:
        return 'None'
    else:
        result = ''
        while node is not None:
            if node.next is not None:
                result += str(node.data) + ' -> '
            else:
                result += str(node.data) + ' -> None'
            node = node.next
        return result