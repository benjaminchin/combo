import random
import networkx as nx
import matplotlib.pyplot as plt
from algos import dijkstra

def generate_graph(n):
    g = nx.Graph()
    for i in range(n):
        for j in range(n):
            if i == j or g.has_edge(i, j) or g.has_edge(j, i):
                continue
            if random.random() < 0.05:
                g.add_edge(i, j, weight=random.randint(10, 100))
    return g

def main():
    g = generate_graph(100)
    print(dijkstra(g, 0, 99))

    # draw node labels
    pos = nx.circular_layout(g)
    nx.draw(g, pos, with_labels=True, font_size=12, node_size=750)

    # draw edge labels
    edge_labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

    # will show graph in new window
    plt.show()

if __name__ == '__main__':
    main()
