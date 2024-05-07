import networkx as nx
import heapq

'''
MATH 3134 Research Project S24
Team Name: TBD Front Left
'''

'''
Dijkstra's Algorithm on a graph G
Calculates the shortest path between vertices source and target.
'''
def dijkstra(G: nx.Graph, source, target):
    minHeap = [(0, source)]
    visited = set()
    
    distances = {node: float('inf') for node in G.nodes}
    distances[source] = 0

    while minHeap:
        d, v = heapq.heappop(minHeap)

        if v in visited:
            continue

        visited.add(v)
        for neighbor in G.neighbors(v):
            weight = G.edges[v, neighbor]['weight']
            distance = d + weight

            if neighbor not in visited and distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(minHeap, (distance, neighbor))

    return distances[target]

'''
Uniform Cost Search algorithm on a graph G
Calculates the shortest path between vertices source and target.
'''
def uniform_cost_search(G: nx.Graph, source, target):
    distances = {source: 0}
    minHeap = [(0, source)]

    while minHeap:
        cost, node = heapq.heappop(minHeap)
        
        if node == target:
            return distances[node]
        
        for neighbor in G.neighbors(node):
            total_cost = cost + G.edges[node, neighbor]['weight']
            if neighbor not in distances or total_cost < distances[neighbor]:
                distances[neighbor] = total_cost
                heapq.heappush(minHeap, (total_cost, neighbor))
                    
    return float('inf') # path not possible

