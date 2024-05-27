'''
Exercise num 5. Regular graphs and Watts-Strogatz model
Part - 1 Regular graphs
Take some regular graphs, for example a complete graph (clique) or a triangular lattice, and compute the diameter and other measures related to clustering, such as the number of triangles (triangles(G)), the transitivity (transitivity(G)), the clustering coefficient of the entire network or of individual nodes.

Plot the degree distribution.

Part - 2
Comparison between Watts-Strogatz and G(N,M)
Generate two random graphs with the same number of nodes N and the same number of links M and compare their characteristics as we have seen in class.
'''


import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


'''Part - 1 '''
# nodes_clique=26
# clique_graph=nx.complete_graph(nodes_clique)
# nx.draw(clique_graph,with_labels=True)
# plt.show()

# if nx.is_connected(clique_graph):
#     diameter = nx.diameter(clique_graph)
# else:
#     diameter = 'Graph is not connected'
#     print(f"Diameter: {diameter}")

# print("\n"+"Graph")    
# num_triangles = sum(nx.triangles(clique_graph).values()) // 3
# print(f"Number of triangles: {num_triangles}")
# print(f"Transitivity: {nx.transitivity(clique_graph)}")
# print(f"Average Clustering: {nx.average_clustering(clique_graph)}")
# print(f"Clustering: {nx.clustering(clique_graph)}")

# degrees = [d for n, d in clique_graph.degree()]
# max_degree = max(degrees)
# min_degree = min(degrees)
# print(f"Maximum degree: {max_degree}")
# print(f"Minimum degree: {min_degree}")


# #Plot the degree distribution
# degree_sequence = sorted([d for n, d in clique_graph.degree()], reverse=True)
# degree_count = nx.degree_histogram(clique_graph)
# plt.bar(range(len(degree_count)), degree_count, width=0.80, color="b", alpha=0.6)
# plt.xlabel('Degree')
# plt.ylabel('Count')
# plt.title('Degree Distribution')
# plt.show()

'''Part - 2 '''

N = 1000   
K = 10     
p = 0.1    
M = (N * K) // 2  # Number of edges in the Erdős-Rényi graph

ws_graph = nx.watts_strogatz_graph(N, K, p)
er_graph = nx.gnm_random_graph(N, M)

def compute_graph_properties(graph):
    properties = {}
    properties['number_of_nodes'] = graph.number_of_nodes()
    properties['number_of_edges'] = graph.number_of_edges()
    properties['average_degree'] = np.mean([d for n, d in graph.degree()])
    properties['diameter'] = nx.diameter(graph) if nx.is_connected(graph) else float('inf')
    properties['average_clustering'] = nx.average_clustering(graph)
    properties['average_shortest_path_length'] = nx.average_shortest_path_length(graph) if nx.is_connected(graph) else float('inf')
    return properties

ws_properties = compute_graph_properties(ws_graph)
er_properties = compute_graph_properties(er_graph)

# Print properties
print("Watts-Strogatz Graph Properties:")
for key, value in ws_properties.items():
    print(f"{key}: {value}")

print("\nErdős-Rényi Graph Properties:")
for key, value in er_properties.items():
    print(f"{key}: {value}")

