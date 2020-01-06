from Exercise5.bacefook_greedy_algorithm import bacefook_greedy_algorithm
from Exercise5.random_graph import graph_randomize


def main(n: int):
    for i in range(0,100):
        print("---- GRAPH ",i+1," ----")
        graph = graph_randomize(100)
        map = bacefook_greedy_algorithm(graph)
        # Prints the result
        sum = 0
        for k in map:
            if map[k]:
                sum += 1
        print("Number of software: ",sum)


if __name__ == '__main__':
    main(100)
