from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if not isinstance(node, Node):
        raise Exception
    current_node = node
    for i in range(index + 1):
        if i == index and current_node.data != None:
            return current_node
        current_node = current_node.next
    raise Exception
    # Your code goes here.
  