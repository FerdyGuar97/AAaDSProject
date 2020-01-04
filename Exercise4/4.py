from RecoursiveExercise4.general_tree import GeneralTree
import time


def bacefook_algorithm(tree: GeneralTree, root: GeneralTree.Position):
    best = {i: [0, 0] for i in tree.postorder()}

    for c in tree.children(root):
        best[c][0], best[c][1] = bacefook_algorithm(tree, c)

    withoutRoot = sum(best[c][1] for c in tree.children(root))
    withRoot = 1 + sum(min(best[c][0], best[c][1]) for c in tree.children(root))

    return (withoutRoot, withRoot)

def main():
    time.sleep(1)
    tree = GeneralTree()
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

    min(bacefook_algorithm(tree, a))

if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time() - start_time)
