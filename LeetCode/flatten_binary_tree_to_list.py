class Solution:

    def dfs(self, root):

        if not root:
            return None

        leftTail = self.dfs(root.left)
        rightTail = self.dfs(root.right)

        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        # We need to return the tail of the list
        if rightTail:
            return rightTail

        if leftTail:
            return leftTail

        return root

    def flatten(self, root) -> None:
        self.dfs(root)
