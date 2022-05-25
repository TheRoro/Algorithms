class Solution:
    def __init__(self):
        self.elements = []

    def inorder(self, root):
        if not root:
            return None

        self.inorder(root.left)
        self.elements.append(root.val)
        self.inorder(root.right)

    def kth_smallest(self, root, k: int) -> int:
        self.inorder(root)
        return self.elements[k - 1]
