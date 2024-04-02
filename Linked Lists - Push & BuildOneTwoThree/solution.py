from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    if not head:
        return Node(data)
    output = Node(data)
    output.next = head
    return output

def build_one_two_three():
    node = push(push(Node(3), 2), 1)
    return node

