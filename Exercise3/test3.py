from time import time, sleep

from TdP_collections.graphs.graph import Graph
from random import Random
from Exercise3.iterative_dfs import iterative_dfs
from TdP_collections.graphs.dfs import DFS


def main(n: int):
    """
        create a graph and call generate graph
        then call iterative DFS and DFS from TdP_collection
    """
    graph = Graph()
    vertices = []

    generate_graph(graph, vertices, n)
    start_time = time()
    sleep(1)
    iterative_dfs(vertices[0], graph)
    print(time() - start_time)

    discovered = {}
    DFS(graph, vertices[0], discovered)
    for v in discovered:
        v.discovered = True
        v.discovery_edge = discovered[v]


def generate_graph(graph: Graph, vertices: [], n: int):
    random = Random()

    for i in range(0, n):
        vertices.append(graph.insert_vertex(i))
    print("Root:" + str(vertices[0]._element))

    for a in range(0, len(vertices)):
        for i in range(0, random.randint(1, 3)):
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


if __name__ == '__main__':
    main(10)
