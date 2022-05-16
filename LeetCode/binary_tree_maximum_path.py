def maxPathSum(root) -> int:
    res = [root.val]

    def get_max_path(root):
        if not root:
            return 0

        left = get_max_path(root.left)
        right = get_max_path(root.right)
        left = max(left, 0)
        right = max(right, 0)

        actual = root.val + left + right
        res[0] = max(res[0], actual)

        return root.val + max(left, right)

    get_max_path(root)
    return res[0]
