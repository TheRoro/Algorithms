class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: 'Node') -> 'Node':
    if not node:
        return None

    graph_map = {}

    first_clone = Node(node.val)

    graph_map[node] = first_clone

    queue = [node]

    while queue:
        original = queue.pop(0)
        clone = graph_map[original]

        for neigh in original.neighbors:
            if neigh not in graph_map:
                graph_map[neigh] = Node(neigh.val)
                queue.append(neigh)

            neigh_clone = graph_map[neigh]
            clone.neighbors.append(neigh_clone)

    return first_clone
