def calc_max_depth(root, depth=0):
    if not root:
        return depth
    return max(calc_max_depth(root.left, depth + 1), calc_max_depth(root.right, depth + 1))


def max_depth(root) -> int:
    return calc_max_depth(root)
