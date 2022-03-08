def rangeSum(root, low, high):
    #         5
    #    3          7
    #  1   4      6      8
    #  low = 1   high = 6

    if not root:
        return 0

    # breadth first search to traverse the tree
    queue = [root]
    range_sum = 0

    while queue:
        node = queue.pop(0)

        # verify if the value of the actual node is in range
        if node.val >= low and node.val <= high:
            range_sum += node.val

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return range_sum

