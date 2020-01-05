from Exercise5.random_graph import graph_randomize
from TdP_collections.graphs.graph import Graph
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from Exercise3.test import plot_graph

def bacefook_algh(graph: Graph):
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


# giusto per sgranchire la mente

def main(n: int):
    graph = graph_randomize(n)
    map = bacefook_algh(graph)
    sum = 0
    for k in map:
        if map[k]:
            sum += 1
    print(map)
    print(sum)
    plot_graph(graph)


if __name__ == '__main__':
    main(100)
