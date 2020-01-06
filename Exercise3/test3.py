from Exercise3.random_graph import graph_randomize
from Exercise3.iterative_dfs import iterative_dfs


def main(n: int):
    """
        create a graph and call generate graph
        then call iterative DFS and DFS from TdP_collection
    """
    graph = graph_randomize( n)
    vertices = [v for v in graph.vertices()]
    iterative_dfs(vertices[0], graph)
    print("Discovery edges: ",[str(v.discovery_edge) for v in graph.vertices()])

if __name__ == '__main__':
    main(10)
