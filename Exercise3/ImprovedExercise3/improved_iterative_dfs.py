from Exercise3.ImprovedExercise3.adja_list_graph import AdjListGraph


def iterative_dfs(startingVertex, graph):
    """Perform DFS of the undiscovered portion of Graph graph starting at Vertex startingVertex."""
    startingVertex.discovered = True
    startingVertex.discovery_edge = AdjListGraph.Edge(startingVertex, None, None)  # Dummy edge
    walk = startingVertex

    while walk is not None:
        adj = graph.incident_edges(walk)
        edge = adj.popleft()
        opposite = edge.opposite(walk)
        if not opposite.discovered:
            opposite.discovered = True
            opposite.discovery_edge = edge
            walk = opposite
            adj.append(edge)
        else:
            walk = walk.discovery_edge.opposite(walk)

    startingVertex.discovery_edge = None  # Remove dummy edge
