'''
Exercise : 1 WarmUp
With this first exercise we make some experience with a graph library. 
I will use NetworkX but you can use any other library of your choice

Install NetworkX (see documentation at: https://networkx.org/documentation/stable/index.html)
Select a graph (see for example https://networkx.org/documentation/stable/auto_examples/index.html#graph)
Compute and print basic graph properties 
(e.g., number of nodes, number of links, diameter, adjacency list)
Draw the graph
Plot the degree distribution
Repeat steps 1-5, reading a graph from an external file 
(see for example the dataset available at https://networkrepository.com/)
'''

import networkx as nx
import matplotlib.pyplot as plt

selected_graph = nx.karate_club_graph()


num_of_nodes=selected_graph.number_of_nodes()
num_of_edges=selected_graph.number_of_edges()
diameter=nx.diameter(selected_graph)
adj_lists=selected_graph.adjacency()


print("Number of edges are: ",num_of_edges)
print("Number of nodes are: ",num_of_nodes)
print("Diameter is : ",diameter)
print("adjacency list is : ")
for node, adjacencies in adj_lists:
    print(f"{node}: {list(adjacencies)}")

#Draw the graph

nx.draw(selected_graph,with_labels=True)
plt.show()


# Plot the degree distribution
degree_sequence = sorted([d for n, d in selected_graph.degree()], reverse=True)
degree_count = nx.degree_histogram(selected_graph)
plt.bar(range(len(degree_count)), degree_count, width=0.80, color="b", alpha=0.6)
plt.xlabel('Degree')
plt.ylabel('Count')
plt.title('Degree Distribution')
plt.show()



'''
Exercise : 2 Betweenesss and Closeness
With this second exercise we continue using the graph library.

Take the graph used for the first exercise.
Compute the betweenness centrality and the closeness centrality for the nodes.
For each metric, print the top-10 nodes with their associated centrality values.
'''

betweeness=nx.betweenness_centrality(selected_graph)
for node, centrality in sorted(betweeness.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"Node: {node}, Betweenness Centrality: {centrality:.4f}")

closeness=nx.closeness_centrality(selected_graph)
for node, centrality in sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"Node: {node}, Closeness Centrality: {centrality:.4f}")




