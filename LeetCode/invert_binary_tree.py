def invert_tree(root):
    if not root:
        return None

    q = [root]

    while q:
        node = q.pop(0)

        node.right, node.left = node.left, node.right

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

    return root
