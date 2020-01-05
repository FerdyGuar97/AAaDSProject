from TdP_collections.graphs.graph import Graph
from random import Random


def graph_randomize(n: int):
    graph = Graph()
    random = Random()
    # This structure allows us to pick vertex randomly
    vertices = []

    for i in range(0,n):
        graph.insert_vertex(i)

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

    print("number of vertices "+str(graph.vertex_count())+"\nnumber of edges "+str(graph.edge_count()))

    return graph
