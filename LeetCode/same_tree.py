def compare_nodes(p, q):
    if not p and not q:
        return True

    if not p or not q or p.val != q.val:
        return False

    return compare_nodes(p.left, q.left) and compare_nodes(p.right, q.right)


def is_same_tree(p, q) -> bool:
    return compare_nodes(p, q)
