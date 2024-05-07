import random
import time
import sys
import networkx as nx
import matplotlib.pyplot as plt
from algos import dijkstra, uniform_cost_search


'''
MATH 3134 Research Project S24
Team Name: TBD Front Left
'''


'''
Generates a simple, connected weighted graph with n vertices.
@return A networkx graph
'''
def generate_graph(n):
    g = nx.Graph()
    nodes = list(range(n))

    # Create a spanning tree first to ensure connected graph
    for i in range(1, n):
        g.add_edge(nodes[i-1], nodes[i], weight=random.randint(1, 10))

    # Add additional edges randomly
    for i in range(n):
        for j in range(i+1, n):
            if not g.has_edge(i, j) and random.random() < 0.05:
                g.add_edge(i, j, weight=random.randint(1, 10))

    return g


'''
Main function. Runs dijkstra and ucs against each other for time.
Plots the networkx graph.
'''
def main():

    if (len(sys.argv) != 4):
        print('Usage: python3 main.py <num_nodes> <source> <target>')
        sys.exit()

    source = int(sys.argv[2])
    target = int(sys.argv[3])
    num_nodes = int(sys.argv[1])

    if source < 0 or target < 0 or num_nodes < 0:
        print('Cannot input negative numbers')
        sys.exit()
    elif source > num_nodes or target > num_nodes:
        print('Cannot have <source> or <target> out of range of <num_nodes>')
        sys.exit()

    g = generate_graph(num_nodes + 1)

    # Run and time dijkstra's alg
    start = time.time()
    length = dijkstra(g, source, target)
    end = time.time()
    print('The shortest path between ' + str(source) + ' and ' + str(target) + ' is: ' + str(length))
    print('Time elapsed (DIJKSTRA): ' + str((end - start) * (10**6)) + ' μs')

    # Run and time uniform cost search alg
    start = time.time()
    length = uniform_cost_search(g, source, target)
    end = time.time()
    print('The shortest path between ' + str(source) + ' and ' + str(target) + ' is: ' + str(length))
    print('Time elapsed (UCS): ' + str((end - start) * (10**6)) + ' μs')

    # set colors
    color_map = []
    for node in g:
        if node == source or node == target:
            color_map.append('red')
        else:
            color_map.append('gray')

    # draw node labels
    pos = nx.spring_layout(g)
    nx.draw(g, pos, node_color=color_map, with_labels=True, font_size=30, node_size=2000)

    # draw edge labels
    edge_labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=16)

    # will show graph in new window
    plt.show()


if __name__ == '__main__':
    main()
