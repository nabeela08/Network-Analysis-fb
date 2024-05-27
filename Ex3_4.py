
# Exercise num 3. Erdős-Rényi random graphs
# In this third exercise we learn how to work with syntectic models.

# We start by generating different Erdős-Rényi random graphs G(N,p) for different values of the parameters, e.g., by varying the number of vertices N or the probability p. 

# For each graph, compute some of the metrics we have already computed in previous exercises and check if it is connected. If the answer is yes, compute also its diameter.

# Plot the degree distribution.

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
# no clustering
#nodes=[4]
#probabilities=[0.8]

nodes=[6]
probabilities=[0.7]
                
for N in nodes:
    for p in probabilities:
        G = nx.erdos_renyi_graph(N, p)

        if nx.is_connected(G):
            diameter=nx.diameter(G)
            print(f"Graph with N={N}, p={p} is connected and diamater for node {N} is {diameter}")
        else:
            print(f"Graph with N={N}, p={p} is not connected.")
            
        print("Number of edges are: ",G.number_of_edges())
        print("Number of nodes are: ",G.number_of_nodes())
        print("Average Degree Connectivity",nx.average_degree_connectivity(G))
        print("Average Clustering",nx.average_clustering(G))
        print("\n")

nx.draw(G,with_labels=True)
plt.show()
# Plot the degree distribution
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = nx.degree_histogram(G)
plt.bar(range(len(degree_count)), degree_count, width=0.80, color="b", alpha=0.6)
plt.xlabel('Degree')
plt.ylabel('Count')
plt.title('Degree Distribution')
plt.show()



# Exercise num 4. Erdős-Rényi random graphs (cnt)
# Consider an Erdős-Rényi random graph with N = 3000 nodes, 
# connected to each other with probability p = 10-3 and then answer to the following questions.

# What is the expected number of links, 〈L〉?
# In which regime is the network?
# Calculate the probability pc so that the network is at the critical point.
# Given the linking probability p = 10-3,
#  calculate the number of nodes Ncr so that the network has only one component.
# For the network in (4), 
# calculate the average degree 〈kcr〉 and the average distance 〈d〉 between two randomly chosen nodes




import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

Nodes=3000
probabilities=0.001
avg_degree=0.0
G=nx.erdos_renyi_graph(Nodes,probabilities)

expected_links = probabilities * (Nodes * (Nodes - 1)) / 2
print(f"Expected Number of Links ⟨L⟩: {expected_links}")


if probabilities < 1 / Nodes:
    regime = "Subcritical"
elif probabilities > 1 / Nodes:
    regime = "Supercritical"
else:
    regime = "Critical Point"
print(f"In which regime is the network: {regime}")


pc = 1 / Nodes
print(f"The critical point probability pc is: {pc}")

if nx.is_connected(G):
    Ncr = Nodes
else:
    components = list(nx.connected_components(G))
    largest_component = max(components, key=len)
    Ncr = len(largest_component)
print(f"Number of nodes Ncr so that the network has only one component: {Ncr}")



if nx.is_connected(G):
    avg_distance = nx.average_shortest_path_length(G)

else:

    largest_subgraph = G.subgraph(largest_component).copy()
    if nx.is_connected(largest_subgraph):
        avg_distance = nx.average_shortest_path_length(largest_subgraph)
    else:
        largest_cc_in_subgraph = max(nx.connected_components(largest_subgraph), key=len)
        largest_cc_subgraph = G.subgraph(largest_cc_in_subgraph).copy()
        avg_distance = nx.average_shortest_path_length(largest_cc_subgraph)
        avg_degree = probabilities * (Ncr - 1)
print(f"Average Distance ⟨d⟩ for Ncr: {avg_distance:.4f}")
print(f"Average Degree ⟨k⟩ for Ncr: {avg_degree:.4f}")

