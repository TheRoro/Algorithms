def connect(root: 'Node') -> 'Node':
    if not root:
        return None

    queue = [root]

    while queue:
        queue_size = len(queue)

        for i in range(queue_size):
            node = queue.pop(0)

            if i + 1 != queue_size:
                node.next = queue[0]

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return root
