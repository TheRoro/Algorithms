class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.index = 0

    @staticmethod
    def serialize(root):
        res = []

        def nodes_to_string(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))

            nodes_to_string(node.left)
            nodes_to_string(node.right)

        nodes_to_string(root)
        return ",".join(res)

    def deserialize(self, data):
        nodes = data.split(",")

        def string_to_nodes():
            if nodes[self.index] == "N":
                self.index += 1
                return None

            node = TreeNode(nodes[self.index])
            self.index += 1
            node.left = string_to_nodes()
            node.right = string_to_nodes()
            return node

        return string_to_nodes()
