from Exercise4.bacefook_dynamic_algorithm import bacefook_dynamic_algorithm
from Exercise4.n_tree import NTree
import time


def main():
    time.sleep(1)
    tree = NTree()
    a = tree.add('A')
    b = tree.add('B', a)
    c = tree.add('C', a)
    d = tree.add('D', a)
    e = tree.add('E', b)
    f = tree.add('F', b)
    g = tree.add('G', e)
    h = tree.add('H', b)
    i = tree.add('I', c)
    l = tree.add('L', c)
    m = tree.add('M', i)
    n = tree.add('N', m)
    o = tree.add('O', l)
    p = tree.add('P', o)
    q = tree.add('Q', o)
    r = tree.add('R', p)

    print(bacefook_dynamic_algorithm(tree))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time() - start_time)
