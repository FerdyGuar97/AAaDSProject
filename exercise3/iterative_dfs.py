from TdP_collections.graphs.graph import Graph


def iterative_dfs(rootNode, graph):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u."""
    rootNode.discovered = True
    rootNode.discoveryEdge = Graph.Edge(rootNode, None, None)  # Dummy edge
    walk = rootNode

    while walk != None:
        hasToGoBack = True
        for edge in graph.incident_edges(walk):
            opposite = edge.opposite(walk)
            if not opposite.discovered:
                opposite.discovered = True
                opposite.discoveryEdge = edge
                walk = opposite
                hasToGoBack = False
                break

        if hasToGoBack:
            walk = walk.discoveryEdge.opposite(walk)

    rootNode.discoveryEdge = None  # Remove dummy edge
