'''
Exercise:9 part 1
'''

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community

# With karate club
G = nx.karate_club_graph()
girvan_newman_communities = list(community.girvan_newman(G))
modularities = [community.modularity(G, communities) for communities in girvan_newman_communities]

best_partition_index = modularities.index(max(modularities))
best_partition = girvan_newman_communities[best_partition_index]

partition_dict = {}
for index, community_nodes in enumerate(best_partition):
    for node in community_nodes:
        partition_dict[node] = index

colors = [partition_dict[node] for node in G.nodes()]

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.rainbow, node_size=500, edge_color='gray')
plt.title('Zachary\'s Karate Club - Girvan-Newman Community Detection')
plt.show()

 # With random graph
random_G = nx.gnp_random_graph(34, 0.1, seed=42, directed=False)

random_girvan_newman_communities = list(community.girvan_newman(random_G))

random_modularities = [community.modularity(random_G, communities) for communities in random_girvan_newman_communities]

random_best_partition_index = random_modularities.index(max(random_modularities))
random_best_partition = random_girvan_newman_communities[random_best_partition_index]

random_partition_dict = {}
for index, community_nodes in enumerate(random_best_partition):
    for node in community_nodes:
        random_partition_dict[node] = index

random_colors = [random_partition_dict[node] for node in random_G.nodes()]

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(random_G)
nx.draw(random_G, pos, node_color=random_colors, with_labels=True, cmap=plt.cm.rainbow, node_size=500, edge_color='gray')
plt.title('Random Graph - Girvan-Newman Community Detection')
plt.show()

