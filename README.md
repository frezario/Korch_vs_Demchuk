# Kruskal vs Prim

![prim-kruskal](https://user-images.githubusercontent.com/91615650/154838046-16c67c3c-fa0a-4d13-ab47-86da31040bbb.png)

The core purpose of this project is a comparison of two spanning tree building algorithms - Kruskal and Prim.

There are 4 Python modules, namely:

```create_graph.py``` - a module that contains gnp_random_connected_graph() function to generate random graphs.

```kruskal_algorithm.py``` - a module that contains kruskal_algorithm() function to seek for spanning tree in a graphs and two supportive functions.

An example of spanning tree generated:

![image](https://user-images.githubusercontent.com/91615650/154845615-ec98f5ac-15ad-4b43-b8eb-a62680270b4b.png)

```prim_algorithm.py``` - a module that contains prim_algorithm() function to seek for spanning tree in a graphs.

An example of spanning tree generated:

![image](https://user-images.githubusercontent.com/91615650/154845701-0c88265f-32d8-4bff-a059-56d413260c04.png)

```time_measurement.py``` - a module to compare two algorithms.

To make a detailed comparison of two algorithms, you should run time_measurement.py.

The console will appear and ask you to pass several pieces of data and then it will display the average time of each algorithm:

![image](https://user-images.githubusercontent.com/91615650/154846036-4ec9a177-d9a1-42a2-8e68-d2d4b9de7ee9.png)

After, it will ask you if you'd like to plot a graph with statistics. If positive answer received, the plotting will begin. Ecentually, it will display a graph.

(Note: the graph completeness and number of iterations will reamin the same).

Results for certain values:

![image](https://user-images.githubusercontent.com/91615650/154844282-a9bb912f-fcb7-4571-aca3-b3de258fc956.png)

![image](https://user-images.githubusercontent.com/91615650/154844387-34e18cdd-558f-44be-8cb7-b4e05980138a.png)
