from TdP_collections.graphs.graph import Graph
from random import Random


def graph_randomize(n: int):
    graph = Graph()
    random = Random()

    for i in range(0,n):
        graph.insert_vertex(i)

    for v in graph.vertices():
        for u in graph.vertices():
            if bool(random.getrandbits(1)) and u != v and graph.get_edge(u,v) is None:
                graph.insert_edge(u,v)

    print("number of vertices "+str(graph.vertex_count())+"\nnumber of edges "+str(graph.edge_count()))

    return graph
