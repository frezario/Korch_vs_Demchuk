import random
from itertools import combinations, groupby
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree


def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: float,
                               draw: bool = False):
    """
    Generates a random undirected graph, similarly to an E
    ,rdős-Rényi graph, but enforcing that the resulting graph
    is conneted
    """

    edges = combinations(range(num_of_nodes), 2)
    G = nx.Graph()
    G.add_nodes_from(range(num_of_nodes))

    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)

    for (u, v, w) in G.edges(data=True):
        w['weight'] = random.randint(0, 10)

    if draw:
        plt.figure(figsize=(10, 6))
        nx.draw(G, node_color='lightblue',
                with_labels=True,
                node_size=500)
        plt.show()
    return G

G = gnp_random_connected_graph(10, 0.4, False)


mstk = tree.minimum_spanning_tree(G, algorithm="kruskal")


nx.draw(mstk, node_color='lightblue',
        with_labels=True,
        node_size=500)

print(mstk.edges(), len(mstk.edges()))

mstp = tree.minimum_spanning_tree(G, algorithm="prim")

nx.draw(mstp, node_color='lightblue',
        with_labels=True,
        node_size=500)

print(mstp.edges(), len(mstp.edges()))

edges = list(G.edges())

edges[:5]