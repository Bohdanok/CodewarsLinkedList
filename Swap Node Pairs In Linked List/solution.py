from preloaded import Node

def swap_pairs(head):
    print(head)
    if not head:
        return
    cur_node, next_node = head, head.next
    if not next_node:
        return cur_node
    output_node = Node()
    bound = 0
    while next_node:
        count = 0
        cur_node.next = next_node.next
        next_node.next = cur_node
        cur_output_node = output_node
        while cur_output_node.next:
            cur_output_node = cur_output_node.next
            if count == bound - 1:
                break
            count += 1
        cur_output_node.next = next_node
        bound += 2
        if cur_node.next:
            cur_node, next_node = cur_node.next, cur_node.next.next
        else: break
    return output_node.next