# Graph Theory Network Analysis

This repository contains a Python script to analyze a Facebook-like social network using graph theory. The script performs various network analysis tasks, including computing basic metrics, identifying communities, and visualizing degree distributions.

## Table of Contents

- [Introduction to Graph Theory](#introduction-to-graph-theory)
- [Network Metrics](#network-metrics)
  - [Number of Nodes and Edges](#number-of-nodes-and-edges)
  - [Average Degree](#average-degree)
  - [Clustering Coefficient](#clustering-coefficient)
  - [Assortativity](#assortativity)
  - [Diameter](#diameter)
  - [Density](#density)
  - [Centrality Measures](#centrality-measures)
- [Community Detection](#community-detection)
- [Degree Distribution](#degree-distribution)
- [Usage](#usage)
- [Requirements](#requirements)

## Introduction to Graph Theory

Graph theory is a field of mathematics focused on the properties of graphs. A graph is a collection of nodes (or vertices) connected by edges (or links). In the context of network analysis, graphs are used to model relationships between entities, such as friendships in a social network.

## Network Metrics

### Number of Nodes and Edges

- **Nodes**: The entities in the network (e.g., users in a social network).
- **Edges**: The connections between the nodes (e.g., friendships).

### Average Degree

The average degree of a node in the network is the average number of connections each node has. It is calculated as:

\[ \text{Average Degree} = \frac{2 \times \text{Number of Edges}}{\text{Number of Nodes}} \]

### Clustering Coefficient

The clustering coefficient measures the tendency of nodes to form clusters or groups. It is the fraction of possible triangles through a node that exist.

### Assortativity

Assortativity measures the tendency of nodes to connect with other similar nodes. For example, in a social network, it might measure the extent to which people tend to be friends with others of the same age.

### Diameter

The diameter of a network is the longest shortest path between any two nodes. It gives an indication of the "size" of the network in terms of path length.

### Density

Density is the ratio of the number of edges to the number of possible edges in the graph. It indicates how connected the graph is:

\[ \text{Density} = \frac{2 \times \text{Number of Edges}}{\text{Number of Nodes} \times (\text{Number of Nodes} - 1)} \]

### Centrality Measures

Centrality measures identify the most important nodes in a network. Common centrality measures include:

- **Degree Centrality**: Number of connections a node has.
- **Betweenness Centrality**: Number of times a node acts as a bridge along the shortest path between two other nodes.
- **Closeness Centrality**: How close a node is to all other nodes in the network.

## Community Detection

Community detection involves finding groups of nodes that are more densely connected to each other than to the rest of the network. The Louvain method is a popular algorithm for detecting communities.

## Degree Distribution

The degree distribution of a network is the probability distribution of the degrees over the entire network. It shows how the connections are distributed among the nodes.

## Usage

To use the script in this repository, follow these steps:

1. Clone the repository:
   git clone https://github.com/yourusername/network-analysis.git
   cd network-analysis
2. Install the required packages:
pip install -r requirements.txt

3. Run the analysis script:
python analysis.py
The results, including various metrics and visualizations, will be saved to the output files.
