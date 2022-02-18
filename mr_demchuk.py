'''
    Prim algorithm. Created by Mr.Demchuk.
    All rights preserved.
'''
import networkx as nx
import create_graph
from itertools import combinations


def prim_algorithm(graph:nx.Graph) -> nx.Graph:
    """
    Generates a minimum spanning tree and returns it.
    Args:
        graph (nx.Graph): a graph in which we want
        to find the minimum spanning tree.
    Returns:
        nx.Graph: a spanning tree found.
    Example:
    >>> prim_algorithm(nx.Graph([(1,2,{'weight':1}),(1,3,{'weight':2}),(2,3,{'weight':0})])).edges(data=True)
    EdgeDataView([(1, 2, {'weight': 1}), (2, 3, {'weight': 0})])
    """
    spanning_tree = nx.Graph()
    # Adding starting point to a tree
    spanning_tree.add_node(list(graph.nodes)[0])
    while len(spanning_tree.nodes) != len(graph.nodes):
        # Searching for incident edges to nodes of already built tree
        incident_edges = list(graph.edges(spanning_tree.nodes, data=True))
        # Deleting those that would form a circuit
        cyclic_edges = set(combinations(spanning_tree.nodes, 2))
        incident_edges = [edge for edge in incident_edges if (edge[0], edge[1]) not in cyclic_edges]
        # Searching for a cheapest edge, which is incident to already added nodes
        min_edge = min(incident_edges, key=lambda edge: edge[2]['weight'])
        # Adding it to our tree
        spanning_tree.add_edge(min_edge[0], min_edge[1], weight = min_edge[2]['weight'])
        # Removing it from our graph
        graph.remove_edge(min_edge[0], min_edge[1])
    return spanning_tree
