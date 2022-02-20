"""A module that creates a minimum spanning tree using kruskal algorithm.
Created by Mr. Korch. (c)
"""
import create_graph
import networkx as nx


def different_sets(vert_sets: list, first_vert: int, second_vert: int):
    """
    Checks whether 'first_vert' and 'second_vert' are in different sets
    in list of sets 'vert_sets'.
    Args:
        vert_sets (set): a list of sets of vertices
        first_vert (int): a first vertice
        second_vert (int): a second vertice
    Returns:
        bool value: True (different sets) or False (same set)
    """
    for part in vert_sets:
        if first_vert in part or second_vert in part:
            if first_vert in part and second_vert in part: #if set([first_vert, second_vert]).issubset(part):
                return False
            return True


def change_sets(vert_sets: set, first_vert: int, second_vert: int):
    """
    Connects two sets into one. One set must contain first vertice,
    and another one the second vertice. Returns a list of sets
    Args:
        vert_sets (set): list of sets with vertices
        first_vert (int): a first vertice
        second_vert (int): a second vertice
    Returns:
        A list of sets with united mutual vertices.
    >>> len(change_sets([{1, 2}, {3, 4, 5}, {6, 7}], 1, 7))
    2
    """
    to_connect = set()
    res = list()
    i = 0
    for part in vert_sets:
        if i < 2:
            if first_vert in part or second_vert in part:
                to_connect |= part
                i += 1
            else:
                res.append(part)
        else:
            res.append(part)
    return res + [to_connect]


def kruskal_algorythm(graph: nx.Graph):
    """
    An algorythym that returns a minimun-weigh
    spanning tree of a connected graph 'graph'.
    Args:
        graph (nx.Graph): a grapth (class networkx.Graph)
    Returns:
        a graph: spanning tree with minimum weight (class networkx.Graph)
    """
    spanning_tree = nx.Graph()

    edges_weight = sorted(graph.edges(data=True), key=lambda x: x[2]["weight"])
    quantity_of_vertcies = len(graph.nodes())
    all_sets = [set([vertice]) for vertice in range(quantity_of_vertcies)]

    chosen_edges = 0
    for elem in edges_weight:
        if different_sets(all_sets, elem[0], elem[1]):
            spanning_tree.add_edge(elem[0], elem[1])
            chosen_edges += 1
            if chosen_edges == quantity_of_vertcies - 1:
                return spanning_tree
            all_sets = change_sets(all_sets, elem[0], elem[1])
