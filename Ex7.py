'''
Write a Python script that, given a network, computes the degree of each node and the average degree of its neighbors and check the results you obtain.
'''
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def create_er_graph(n, p):
    G = nx.erdos_renyi_graph(n, p)
    return G

def compute_average_neighbor_degree(G):
    avg_neighbor_degrees = {}
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        if len(neighbors) > 0:
            avg_neighbor_degree = np.mean([G.degree(neighbor) for neighbor in neighbors])
        else:
            avg_neighbor_degree = 0
        avg_neighbor_degrees[node] = avg_neighbor_degree
    return avg_neighbor_degrees

def check_and_observe_friendship_paradox(G):
    degrees = dict(G.degree())
    avg_neighbor_degrees = compute_average_neighbor_degree(G)

    paradoxical_nodes = []
    for node in G.nodes():
        if avg_neighbor_degrees[node] > degrees[node]:
            paradoxical_nodes.append(node)

    if paradoxical_nodes:
        print("Friendship Paradox is observed in the network.")
        print(f"Nodes where the paradox is observed: {paradoxical_nodes}")
        return True
    else:
        print("Friendship Paradox is NOT observed in the network.")
        return False

# Plotting the results to visualize the Friendship Paradox
def plot_friendship_paradox(degrees, avg_neighbor_degrees):
    nodes = list(degrees.keys())
    node_degrees = list(degrees.values())
    neighbor_avg_degrees = list(avg_neighbor_degrees.values())

    plt.figure(figsize=(10, 6))
    plt.scatter(node_degrees, neighbor_avg_degrees, alpha=0.5)
    plt.plot([min(node_degrees), max(node_degrees)], [min(node_degrees), max(node_degrees)], 'r--', lw=2)
    plt.xlabel('Node Degree')
    plt.ylabel('Average Neighbor Degree')
    plt.title('Friendship Paradox: Node Degree vs. Average Neighbor Degree')
    plt.show()

G = create_er_graph(20, 0.2)

if check_and_observe_friendship_paradox(G):
    degrees = dict(G.degree())
    avg_neighbor_degrees = compute_average_neighbor_degree(G)
    plot_friendship_paradox(degrees, avg_neighbor_degrees)
