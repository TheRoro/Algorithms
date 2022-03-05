class Solution:
    def dfs(self, root):
        if not root:
            return None

        if root.left and not root.left.left and not root.left.right:
            self.leftLeavesSum += root.left.val
            print(self.leftLeavesSum)

        self.dfs(root.left)
        self.dfs(root.right)

    def sumOfLeftLeaves(self, root) -> int:
        self.leftLeavesSum = 0

        self.dfs(root)

        return self.leftLeavesSum
