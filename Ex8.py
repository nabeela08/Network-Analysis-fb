
import networkx as nx
import matplotlib.pyplot as plt

#random directed graph
G = nx.gnp_random_graph(100, 0.05, directed=True)

pagerank_scores = nx.pagerank(G, alpha=0.85)

hits_scores = nx.hits(G)

hub_scores = hits_scores[0]
authority_scores = hits_scores[1]

top_10_pagerank = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)[:10]
top_10_hubs = sorted(hub_scores.items(), key=lambda x: x[1], reverse=True)[:10]
top_10_authorities = sorted(authority_scores.items(), key=lambda x: x[1], reverse=True)[:10]


plt.figure(figsize=(14, 7))

# Plot PageRank
plt.subplot(131)
pagerank_values = list(pagerank_scores.values())
nx.draw(G, pos=nx.spring_layout(G), node_color=pagerank_values, node_size=[v * 10000 for v in pagerank_values], cmap=plt.cm.Blues, with_labels=True)
plt.title('PageRank')

# Plot Hubs
plt.subplot(132)
hub_values = list(hub_scores.values())
nx.draw(G, pos=nx.spring_layout(G), node_color=hub_values, node_size=[v * 10000 for v in hub_values], cmap=plt.cm.Reds, with_labels=True)
plt.title('Hubs')

# Plot Authorities
plt.subplot(133)
authority_values = list(authority_scores.values())
nx.draw(G, pos=nx.spring_layout(G), node_color=authority_values, node_size=[v * 10000 for v in authority_values], cmap=plt.cm.Greens, with_labels=True)
plt.title('Authorities')

plt.show()


print("Top-10 nodes by PageRank:")
for node, score in top_10_pagerank:
    print(f"Node: {node}, PageRank: {score}")

print("\nTop-10 nodes by Hubs:")
for node, score in top_10_hubs:
    print(f"Node: {node}, Hub Score: {score}")

print("\nTop-10 nodes by Authorities:")
for node, score in top_10_authorities:
    print(f"Node: {node}, Authority Score: {score}")

