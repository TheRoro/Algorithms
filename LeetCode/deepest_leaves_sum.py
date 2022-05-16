def deepest_leaves_sum(root) -> int:
    if not root:
        return 0

    queue = [root]
    levels_sum = 0

    while queue:
        queue_size = len(queue)
        actual_sum = 0
        for i in range(queue_size):
            node = queue.pop(0)

            actual_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        levels_sum = actual_sum

    return levels_sum
