class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    odd, even, count = [], [], 1
    while head:
        if count & 1:
            odd.append(head.data)
            
        else:
            even.append(head.data)
        head = head.next
        count += 1
    def add_a_node(list_of_values):
        if not list_of_values:
            return
        n = Node(list_of_values[0])
        n.next = add_a_node(list_of_values[1:])
        return n
    return Context(add_a_node(odd), add_a_node(even))
