class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    string, current_node = "", node
    print(current_node)
    while current_node != None:
        string += str(current_node.data) + ' -> '
        current_node = current_node.next
    return string + 'None'
