import graphviz as gv

def drawAdjListGraph(G):
    dot = gv.Digraph(strict=True)
    n = len(G)
    for u in range(n):
        for v, w in G[u]:
            dot.edge(str(u), str(v), label=str(w))
    
    dot.graph_attr['rankdir'] = 'LR'
    return dot

adj = [[(1, 4), (7, 8)], [(0, 4), (2, 8), (7, 11)], [(1, 8), (3, 7), (5, 4), (8, 2)], [(2, 7), (4, 9), (5, 14)], [(3, 9), (5, 10)], [(2, 4), (3, 14), (4, 10), (6, 2)], [(5, 2), (7, 1), (8, 6)], [(0, 8), (1, 11), (6, 1), (8, 7)], [(2, 2), (6, 6), (7, 7)]]

drawAdjListGraph(adj)