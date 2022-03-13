def isBipartite(graph):
    # -1: gray (not visited)
    # 0: blue (set A)
    # 1: red (set B)

    colors = [-1] * (len(graph))

    for i in range(len(graph)):
        if colors[i] == -1:
            node = (i, 0)  # (node val, node color)
            queue = [node]

            while queue:
                node, color = queue.pop(0)

                if colors[node] == -1:
                    colors[node] = color
                    for neighbor in graph[node]:
                        if colors[neighbor] == -1:
                            queue.append((neighbor, color ^ 1))

                        if colors[neighbor] == color:
                            return False

    return True
