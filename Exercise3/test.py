# Author: Aric Hagberg (hagberg@lanl.gov)
from TdP_collections.graphs.graph import Graph
from random import Random
from Exercise3.iterative_dfs import iterative_dfs
from TdP_collections.graphs.dfs import DFS

def main(n: int):
    graph = Graph()
    random = Random()
    vertices = []

    for i in range(0,n):
        vertices.append(graph.insert_vertex(i))
    print("Root:"+str(vertices[0]._element))

    for a in range(0,len(vertices)):
        for i in range(0,random.randint(1,3)):
            do = True
            while do:
                b = random.randint(0, len(vertices) - 1)
                if b == a:
                    continue
                try:
                    graph.insert_edge(vertices[a], vertices[b])
                except ValueError:
                    continue
                do = False

    plot_graph(graph)
    iterative_dfs(vertices[0],graph)
    plot_graph(graph)
    
    discovered = {}
    DFS(graph,vertices[0],discovered)
    for v in graph.vertices():
        v.discovered = True
        v.discoveryEdge = discovered[v]
    plot_graph(graph)
    print("FINO ALLA FINE")

import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(graph: Graph):
    G = nx.Graph()

    for edge in graph.edges():
        G.add_edge(edge._origin._element, edge._destination._element, discovered = (edge._destination.discoveryEdge == edge or edge._origin.discoveryEdge == edge))

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['discovered'] == True]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['discovered'] == False]

    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge,
                           width=6)
    nx.draw_networkx_edges(G, pos, edgelist=esmall,
                           width=6, alpha=0.5, edge_color='b', style='dashed')

    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main(10)