def level_order(root):
    if not root:
        return []
    # popleft, pop(0). Both are O(1)
    queue = [root]
    levels = []

    while queue:
        queue_size = len(queue)
        level_list = []
        for i in range(queue_size):
            node = queue.pop(0)
            # values of the nodes
            level_list.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        levels.append(level_list)

    return levels
