from Exercise5.bacefook_greedy_algorithm import bacefook_greedy_algorithm
from Exercise5.random_graph import graph_randomize


def main(n: int):
    graph = graph_randomize(n)
    map = bacefook_greedy_algorithm(graph)
    sum = 0
    for k in map:
        if map[k]:
            sum += 1
    print(map)
    print(sum)


if __name__ == '__main__':
    main(100)
