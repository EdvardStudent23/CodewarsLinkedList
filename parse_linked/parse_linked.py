def linked_list_from_string(s):
    if s == "None":
        return None
    nodes = []
    for value in s.split(' -> '):
        if value != 'None':
            nodes.append(Node(int(value)))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]