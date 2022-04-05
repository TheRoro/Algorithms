class Solution:

    def findPath(self, actualSum, root):
        if not root:
            return 0

        actualSum -= root.val

        if not root.left and not root.right:
            if actualSum == 0:
                return True

        return self.findPath(actualSum, root.left) or self.findPath(actualSum, root.right)

    def hasPathSum(self, root, targetSum) -> bool:
        return self.findPath(targetSum, root)
