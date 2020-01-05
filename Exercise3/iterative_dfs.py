from TdP_collections.graphs.graph import Graph


def iterative_dfs(starting_vertex, graph):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u."""
    starting_vertex.discovered = True
    starting_vertex.discovery_edge = Graph.Edge(starting_vertex, None, None)  # Dummy edge
    walk = starting_vertex

    while walk is not None:
        has_to_go_back = True
        for edge in graph.incident_edges(walk):
            opposite = edge.opposite(walk)
            if not opposite.discovered:
                opposite.discovered = True
                opposite.discovery_edge = edge
                walk = opposite
                has_to_go_back = False
                break

        if has_to_go_back:
            walk = walk.discovery_edge.opposite(walk)

    starting_vertex.discovery_edge = None  # Remove dummy edge
