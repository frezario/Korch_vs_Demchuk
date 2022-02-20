import time
import create_graph
from networkx.algorithms import tree
from tqdm import tqdm


NUM_OF_ITERATIONS = 1000


time_taken = 0
for i in tqdm(range(NUM_OF_ITERATIONS)):

    # note that we should not measure time of graph creation
    G = create_graph.gnp_random_connected_graph(100, 0.1, False)

    start = time.time()
    tree.minimum_spanning_tree(G, algorithm="prim")
    end = time.time()

    time_taken += end - start

time_taken / NUM_OF_ITERATIONS
