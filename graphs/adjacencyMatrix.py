import numpy as np
import networkx as nx

G = [[0, 1, 0, 1], 
     [0, 0, 0, 1], 
     [0, 1, 0, 1], 
     [0, 1, 0, 0]]

def showG(G, directed=True):
    g = nx.DiGraph() if directed else nx.Graph()
    n = len(G)
    for u in range(n):
        g.add_node(u)
    for v in range(n):
        if G[u][v] != 0:
            g.add_edge(u,v)
    nx.draw(g, with_labels = True)

showG(G)