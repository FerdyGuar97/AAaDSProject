from TdP_collections.graphs.graph import Graph


def iterative_dfs(rootNode, graph):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u."""
    rootNode.discovered = True
    rootNode.discovery_edge = Graph.Edge(rootNode, None, None)  # Dummy edge
    walk = rootNode

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

    rootNode.discovery_edge = None  # Remove dummy edge
