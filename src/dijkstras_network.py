import networkx as nx
import matplotlib.pyplot as plt
from algos import dijkstra

G = nx.Graph()

# Flight 1 (ROA -> IAD -> YYZ -> YVR -> SYD)
G.add_edge('ROA', 'IAD', weight=177)
G.add_edge('IAD', 'YYZ', weight=346)
G.add_edge('YYZ', 'YVR', weight=2085)
G.add_edge('YVR', 'SYD', weight=7757)

# Flight 2 (ROA -> CLT -> LAX -> SYD)
G.add_edge('ROA', 'CLT', weight=199)
G.add_edge('CLT', 'LAX', weight=2125)
G.add_edge('LAX', 'SYD', weight=7488)

# Flight 3 (ROA -> ATL -> LAX -> SYD)
G.add_edge('ROA', 'ATL', weight=357)
G.add_edge('ATL', 'LAX', weight=1946)

# Flight 4 (ROA -> PHL -> LAX - SYD)
G.add_edge('ROA', 'PHL', weight=311)
G.add_edge('PHL', 'LAX', weight=2401)

# Flight 5 (ROA -> CLT -> DFW -> SYD)
G.add_edge('CLT', 'DFW', weight=936)
G.add_edge('DFW', 'SYD', weight=8578)

# Flight 6 (ROA -> LGA -> DFW -> SYD)
G.add_edge('ROA', 'LGA', weight=405)
G.add_edge('LGA', 'DFW', weight=1389)

# Flight 7 (ROA -> CLT -> DFW -> LAX -> SYD)
G.add_edge('DFW', 'LAX', weight=1235)

# Flight 8 (ROA -> CLT -> IAH -> LAX -> SYD)
G.add_edge('CLT', 'IAH', weight=913)
G.add_edge('IAH', 'LAX', weight=1379)

# Flight 9 (ROA -> IAD -> LAX -> SYD)
G.add_edge('IAD', 'LAX', weight=2288)

# Flight 10 (ROA -> CLT -> STL -> LAX -> SYD)
G.add_edge('CLT', 'STL', weight=575)
G.add_edge('STL', 'LAX', weight=1592)

# Flight 11 (ROA -> IAD -> SFO -> SYD)
G.add_edge('IAD', 'SFO', weight=2419)
G.add_edge('SFO', 'SYD', weight=7417)

# Flight 12 (ROA -> ORD -> LAX -> SYD)
G.add_edge('ROA', 'ORD', weight=531)
G.add_edge('ORD', 'LAX', weight=1745)

# Flight 13 (ROA -> ORD -> SFO -> SYD)
G.add_edge('ORD', 'SFO', weight=1846)

# Flight 14 (ROA -> ATL -> ICN -> SYD)
G.add_edge('ATL', 'ICN', weight=7153)
G.add_edge('ICN', 'SYD', weight=5164)

# Flight 15 (ROA -> ORD -> HND -> SYD)
G.add_edge('ORD', 'HND', weight=6305)
G.add_edge('HND', 'SYD', weight=4837)

# draw node labels
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_size=12, node_size=750)

# draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# will show graph in new window
plt.show()

# ex. ('ROA', 'IAD'): 177 for one edge
#edges = nx.get_edge_attributes(G, 'weight')
#print(edges)

# ex. ('ROA', 'IAD') for one edge
#edges_no_weight = list(G.edges())
#print(edges_no_weight)

print("The shortest path from ROA to LAX is: " + str(dijkstra(G, 'ROA', 'LAX')))
