import networkx as nx
import matplotlib.pyplot as plt
import time
import heapq

def main():
    """ test_graph = nx.Graph()
    test_graph.add_edge('A', 'B', weight=1)
    test_graph.add_edge('A', 'C', weight=4)
    test_graph.add_edge('B', 'C', weight=2)
    
    start_test = time.time()
    res = dijkstra(test_graph, 'A', 'C')
    end_test = time.time()
    time_test = (end_test - start_test) * float(10^3)
    
    print("It takes Djikstra's algorithm " + str(time_test) + " ms to process")
    print("The shortest path from A to C is " + str(res) + " units") """
    
    # create the graph containing all flight possibilities from Google Flights for ROA -> SYD
    graph = create_graph()
    
    # log processing time of the djikstras function
    start_fun1 = time.time()
    djikstras_res = dijkstra(graph, 'SYD', 'ROA')
    stop_fun1 = time.time()
    time_fun1 = (stop_fun1 - start_fun1) * float(10^3)
    
    # print out number of miles for path, the route it took (TO DO), and the processing time
    print("The shortest path from ROA to SYD is " + str(djikstras_res) + " miles")
    print("It takes Djikstra's algorithm " + str(time_fun1) + " ms to process")
    
    # display graph
    # draw_graph(graph)
    
def create_graph():
    
    graph = nx.Graph()

    # Flight 1 (ROA -> IAD -> YYZ -> YVR -> SYD)
    graph.add_edge('ROA', 'IAD', weight=177)
    graph.add_edge('IAD', 'YYZ', weight=346)
    graph.add_edge('YYZ', 'YVR', weight=2085)
    graph.add_edge('YVR', 'SYD', weight=7757)

    # Flight 2 (ROA -> CLT -> LAX -> SYD)
    graph.add_edge('ROA', 'CLT', weight=199)
    graph.add_edge('CLT', 'LAX', weight=2125)
    graph.add_edge('LAX', 'SYD', weight=7488)

    # Flight 3 (ROA -> ATL -> LAX -> SYD)
    graph.add_edge('ROA', 'ATL', weight=357)
    graph.add_edge('ATL', 'LAX', weight=1946)

    # Flight 4 (ROA -> PHL -> LAX - SYD)
    graph.add_edge('ROA', 'PHL', weight=311)
    graph.add_edge('PHL', 'LAX', weight=2401)

    # Flight 5 (ROA -> CLT -> DFW -> SYD)
    graph.add_edge('CLT', 'DFW', weight=936)
    graph.add_edge('DFW', 'SYD', weight=8578)

    # Flight 6 (ROA -> LGA -> DFW -> SYD)
    graph.add_edge('ROA', 'LGA', weight=405)
    graph.add_edge('LGA', 'DFW', weight=1389)

    # Flight 7 (ROA -> CLT -> DFW -> LAX -> SYD)
    graph.add_edge('DFW', 'LAX', weight=1235)

    # Flight 8 (ROA -> CLT -> IAH -> LAX -> SYD)
    graph.add_edge('CLT', 'IAH', weight=913)
    graph.add_edge('IAH', 'LAX', weight=1379)

    # Flight 9 (ROA -> IAD -> LAX -> SYD)
    graph.add_edge('IAD', 'LAX', weight=2288)

    # Flight 10 (ROA -> CLT -> STL -> LAX -> SYD)
    graph.add_edge('CLT', 'STL', weight=575)
    graph.add_edge('STL', 'LAX', weight=1592)

    # Flight 11 (ROA -> IAD -> SFO -> SYD)
    graph.add_edge('IAD', 'SFO', weight=2419)
    graph.add_edge('SFO', 'SYD', weight=7417)

    # Flight 12 (ROA -> ORD -> LAX -> SYD)
    graph.add_edge('ROA', 'ORD', weight=531)
    graph.add_edge('ORD', 'LAX', weight=1745)

    # Flight 13 (ROA -> ORD -> SFO -> SYD)
    graph.add_edge('ORD', 'SFO', weight=1846)

    # Flight 14 (ROA -> ATL -> ICN -> SYD)
    graph.add_edge('ATL', 'ICN', weight=7153)
    graph.add_edge('ICN', 'SYD', weight=5164)

    # Flight 15 (ROA -> ORD -> HND -> SYD)
    graph.add_edge('ORD', 'HND', weight=6305)
    graph.add_edge('HND', 'SYD', weight=4837)
    
    return graph

def draw_graph(G: nx.Graph):
    # draw node labels
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, font_size=12, node_size=750)

    # draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # will show graph in new window
    plt.show()

def dijkstra(G: nx.Graph, source, target):
    minHeap = [(0, source)]
    visited = set()
    
    distances = {node: float('inf') for node in G.nodes}
    distances[source] = 0

    while minHeap:
        d, v, = heapq.heappop(minHeap)
        if v == target:
            return d

        if v in visited:
            continue

        visited.add(v)
        for neighbor in G.neighbors(v):
            weight = G.edges[v, neighbor]['weight']
            distance = d + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(minHeap, (distance, neighbor))
                
    return distances[target]

def bidirectional_dijkstra(G: nx.Graph, source, target):
    heap_start = [(0, source)]
    heap_end = [(0, target)]

    visited_start = set()
    visited_end = set()

    distances_start = {node: float('inf') for node in G.nodes}
    distances_end = {node: float('inf') for node in G.nodes}

    distances_start[source] = 0
    distances_end[target] = 0

# main()
