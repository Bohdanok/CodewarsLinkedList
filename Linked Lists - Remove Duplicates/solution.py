class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return
    cur_node, next_node = head, head.next
    while next_node is not None:
        if cur_node.data == next_node.data:
            cur_node.next = next_node.next
            next_node = next_node.next
        else: cur_node, next_node = cur_node.next, cur_node.next
    return head