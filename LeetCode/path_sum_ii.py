import copy


class Solution:

    def findPaths(self, allPaths, actualPath, actualSum, root):

        if not root:
            return []

        actualSum -= root.val
        actualPath.append(root.val)

        if not root.right and not root.left:
            if actualSum == 0:
                allPaths.append(actualPath)

        self.findPaths(allPaths, copy.deepcopy(actualPath), actualSum, root.left)
        self.findPaths(allPaths, copy.deepcopy(actualPath), actualSum, root.right)

    def pathSum(self, root, targetSum):

        if not root:
            return None

        allPaths = []
        actualPath = []

        self.findPaths(allPaths, actualPath, targetSum, root)

        return allPaths
