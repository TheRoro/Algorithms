def same_tree(q, p):
    if not p and not q:
        return True

    if p and q and p.val == q.val:
        return same_tree(q.left, p.left) and same_tree(q.right, p.right)

    return False


def is_subtree(root, sub_root) -> bool:
    queue = [root]

    while queue:
        node = queue.pop(0)

        if same_tree(node, sub_root):
            return True

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return False
