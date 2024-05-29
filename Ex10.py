import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


num_nodes = 100  # Number of nodes in the graph


beta = 0.3  # Transmission probability
tI = 3      # Minimum infection duration (time steps)
mu = 0.1    # Recovery probability
i0 = 5      # Initial number of infected individuals



G = nx.watts_strogatz_graph(num_nodes, k=4, p=0.1)

node_state = {node: 'S' for node in G.nodes}
infection_start_time = {node: None for node in G.nodes}

initial_infected = np.random.choice(G.nodes, i0, replace=False)
for node in initial_infected:
    node_state[node] = 'I'
    infection_start_time[node] = 0

state_colors = {'S': 'blue', 'I': 'red', 'R': 'green'}

S_count = [num_nodes - i0]
I_count = [i0]
R_count = [0]

fig, ax = plt.subplots()
pos = nx.spring_layout(G)
nodes = nx.draw_networkx_nodes(G, pos, node_color=[state_colors[node_state[node]] for node in G.nodes], ax=ax)
edges = nx.draw_networkx_edges(G, pos, ax=ax)

def update(num):
    new_infected = []
    new_recovered = []
    for node in G.nodes:
        if node_state[node] == 'I':
            if num - infection_start_time[node] >= tI and np.random.rand() < mu:
                new_recovered.append(node)
            else:
                for neighbor in G.neighbors(node):
                    if node_state[neighbor] == 'S' and np.random.rand() < beta:
                        new_infected.append(neighbor)

    for node in new_infected:
        node_state[node] = 'I'
        infection_start_time[node] = num

    for node in new_recovered:
        node_state[node] = 'R'

    S_count.append(sum(1 for state in node_state.values() if state == 'S'))
    I_count.append(sum(1 for state in node_state.values() if state == 'I'))
    R_count.append(sum(1 for state in node_state.values() if state == 'R'))

    node_colors = [state_colors[node_state[node]] for node in G.nodes]
    nodes.set_color(node_colors)
    return nodes,

ani = FuncAnimation(fig, update, frames=range(50), interval=200, blit=True, repeat=False)
plt.show()

plt.figure()
plt.plot(S_count, label='Susceptible')
plt.plot(I_count, label='Infected')
plt.plot(R_count, label='Recovered')
plt.xlabel('Time step')
plt.ylabel('Number of nodes')
plt.legend()
plt.show()
