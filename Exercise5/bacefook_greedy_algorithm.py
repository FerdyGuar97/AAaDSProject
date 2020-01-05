from TdP_collections.graphs.graph import Graph
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


def bacefook_greedy_algorithm(graph: Graph):
    priority_queue = AdaptableHeapPriorityQueue()
    map = {}
    for v in graph.vertices():
        token = priority_queue.add(-graph.degree(v), v)
        map[v] = {'token': token, 'no_sw_count': graph.degree(v), 'has_sw': False}

    for i in range(0, graph.vertex_count()):
        k, v = priority_queue.remove_min()
        if k == 0:
            break
        map[v]['has_sw'] = True
        for e in graph.incident_edges(v):
            adj_v = e.opposite(v)
            if not map[adj_v]['has_sw']:
                map[adj_v]['no_sw_count'] -= 1
                priority_queue.update(map[adj_v]['token'], -map[adj_v]['no_sw_count'], adj_v)

    return {v._element: map[v]['has_sw'] for v in map}