import networkx as nx
import heapq

def main():
    graph = nx.Graph()
    graph.add_edge('A', 'B', weight=1)
    graph.add_edge('A', 'C', weight=4)
    graph.add_edge('B', 'C', weight=2)
    graph.add_edge('B', 'D', weight=5)
    graph.add_edge('C', 'D', weight=1)

    print(dijkstra(graph, 'A', 'D'))

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

if __name__ == '__main__':
    main()
