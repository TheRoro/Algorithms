def diameterOfBinaryTree(self, root) -> int:
    maxDiameter = [0]

    def dfs(root):
        if not root:
            return -1

        left = dfs(root.left)
        right = dfs(root.right)

        maxDiameter[0] = max(maxDiameter[0], left + right + 2)

        return 1 + max(left, right)

    dfs(root)

    return maxDiameter[0]
