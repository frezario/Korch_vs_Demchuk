'''
    Prim algorithm. Created by Mr.Demchuk.
    All rights preserved.
'''
import networkx as nx

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
    spanning_tree.add_node(list(graph.nodes())[0])
    incident_edges = set()
    last_added_node = list(graph.nodes())[0]
    while len(spanning_tree.nodes) != len(graph.nodes):
        # Searching for new incident edges to nodes of already built tree
        new_edges = {(edge[0], edge[1], edge[2]['weight']) for edge in graph.edges(last_added_node, data=True)}
        incident_edges = incident_edges.union(new_edges)
        # print(f"incident_edges: {incident_edges}")
        # Deleting those that would form a circuit
        incident_edges -= {edge for edge in incident_edges if edge[0] in spanning_tree.nodes and edge[1] in spanning_tree.nodes}
        # print(f"incident_edges: {incident_edges}")
        # Searching for a cheapest edge, which is incident to already added nodes
        min_edge = min(incident_edges, key=lambda edge: edge[2])
        # Adding it to our tree
        spanning_tree.add_edge(min_edge[0], min_edge[1], weight = min_edge[2])
        last_added_node = min_edge[0] if min_edge[0] not in list(spanning_tree.nodes) else min_edge[1]
        # Removing it from our graph
        graph.remove_edge(min_edge[0], min_edge[1])
    return spanning_tree
