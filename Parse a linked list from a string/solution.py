class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    s = s.split(' -> ')
    def add_a_node(list_of_values):
        if list_of_values[0] == 'None':
            return
        return Node(int(list_of_values[0]), add_a_node(list_of_values[1:]))
    return add_a_node(s)