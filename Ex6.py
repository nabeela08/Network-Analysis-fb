'''
Exercise num 6. Configuration and Barabási-Albert models
Configuration model

Use the NetworkX function configuration model() to generate a "random pseudograph (graph with parallel edges and self loops) by randomly assigning edges to match the given degree sequence." 

Define a degree sequence
Create the multi graph and print some information
Delete the self loops (see remove_edges_from() and selfloop_edges())
Print some information on the new graph without self loops
Delete also multi edges (see Graph)
Print some information on the simple graph
Repeat starting from step 1

Barabási-Albert model
Generate Barabási-Albert networks for different values of the parameters using one of the functions provided by the NetworkX library, see for example barabasi_albert_graph().
Compute measures like the degree of the most important hubs, global clustering or the diameter of the resulting networks
Build and analyse the histogram of the degree distribution
Plot in log-log scale
'''
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Configuration Model
def configuration_model_example(degree_sequence):
    # Step 2: Create a multi-graph
    G = nx.configuration_model(degree_sequence)
    print("Configuration Model")
    print("Initial Graph")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Number of self-loops: {nx.number_of_selfloops(G)}")
    
    # Step 3: Remove self-loops
    G.remove_edges_from(nx.selfloop_edges(G))
    print("Graph after removing self-loops")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    
    # Step 4: Remove multi-edges
    G_simple = nx.Graph(G)  # Convert to simple graph
    print("Simple graph after removing multi-edges")
    print(f"Number of nodes: {G_simple.number_of_nodes()}")
    print(f"Number of edges: {G_simple.number_of_edges()}")
    
    return G_simple

degree_sequence = [3, 3, 2, 2, 2, 1, 1, 1, 1]  # Example degree sequence
simple_graph = configuration_model_example(degree_sequence)

# Repeat with different degree sequences
degree_sequence_2 = [4, 3, 3, 3, 2, 2, 1, 1, 1]  # Another example degree sequence
simple_graph_2 = configuration_model_example(degree_sequence_2)

# Barabási-Albert Model
def barabasi_albert_example(n, m):
    # Generate Barabási-Albert network
    BA_G = nx.barabasi_albert_graph(n, m)
    print("Barabási-Albert Graph")
    print(f"Number of nodes: {BA_G.number_of_nodes()}")
    print(f"Number of edges: {BA_G.number_of_edges()}")
    
    # Compute measures
    degrees = [BA_G.degree(n) for n in BA_G.nodes()]
    max_degree = max(degrees)
    clustering_coeff = nx.average_clustering(BA_G)
    diameter = nx.diameter(BA_G)
    
    print(f"Maximum degree: {max_degree}")
    print(f"Global clustering coefficient: {clustering_coeff}")
    print(f"Diameter: {diameter}")
    
    # Degree distribution histogram
    plt.hist(degrees, bins=np.arange(0, max_degree+1) - 0.5, edgecolor='black', density=True)
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.title('Degree Distribution')
    plt.show()
    
    # Degree distribution log-log plot
    degree_counts = np.bincount(degrees)
    degrees = np.nonzero(degree_counts)[0]
    counts = degree_counts[degrees]
    plt.figure()
    plt.loglog(degrees, counts, 'bo', markerfacecolor='none')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.title('Degree Distribution (log-log scale)')
    plt.show()

# Example parameters
n = 1000  # Number of nodes
m = 3     # Number of edges to attach from a new node to existing nodes

barabasi_albert_example(n, m)
