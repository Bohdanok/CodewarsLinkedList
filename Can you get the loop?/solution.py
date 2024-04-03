def loop_size(node):
    fast_ponomarenko, slow_ponomarenko = node, node.next.next
    while fast_ponomarenko != slow_ponomarenko:
        fast_ponomarenko = fast_ponomarenko.next
        slow_ponomarenko = slow_ponomarenko.next.next
    count = 0
    fast_ponomarenko = fast_ponomarenko.next
    slow_ponomarenko = slow_ponomarenko.next.next
    while fast_ponomarenko != slow_ponomarenko:
        fast_ponomarenko = fast_ponomarenko.next
        slow_ponomarenko = slow_ponomarenko.next.next
        count += 1
    return count + 1