from NotImprovedExercise3.adja_list_graph import AdjListGraph
# No fra sono finito nella stessa complessità, ciaone proprio

def iterative_dfs(starting_vertex, graph):
    """Perform DFS of the undiscovered portion of Graph graph starting at Vertex starting_vertex."""
    starting_vertex.discovered = True
    starting_vertex.discovery_edge = AdjListGraph.Edge(starting_vertex, None, None)  # Dummy edge
    walk = starting_vertex

    while walk is not None:
        adj = graph.incident_edges(walk)
        edge = adj[0]
        print("Traversing edge {}".format(edge.endpoints()))
        print("Walk: ",walk)
        opposite = edge.opposite(walk)
        if not opposite.discovered:
            opposite.discovered = True
            opposite.discovery_edge = edge
            print("Opposite: ",opposite)
            walk = opposite
            adj.rotate()
        else:
            walk = walk.discovery_edge.opposite(walk)

    starting_vertex.discovery_edge = None  # Remove dummy edge
