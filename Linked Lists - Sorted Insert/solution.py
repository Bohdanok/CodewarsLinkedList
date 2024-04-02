""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if not head:
        return Node(data)
    prev_node, next_node = head, head.next
    if data < prev_node.data:
            n = Node(data)
            n.next = prev_node
            return n
    while next_node:
        if prev_node.data < data < next_node.data:
            nen = Node(data)
            nen.next = next_node
            prev_node.next = nen
            return head
        prev_node, next_node = prev_node.next, next_node.next
    prev_node.next = Node(data)
    return head