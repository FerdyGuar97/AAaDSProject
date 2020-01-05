from RecoursiveExercise4.general_tree import GeneralTree
import time


def bacefook_algorithm(tree: GeneralTree, root: GeneralTree.Position, best):
    # La tabella deve essere intepretata come segue:
    # Ogni colonna rappresenta un nodo figlio di root,
    # ed in ogni cella è contenuto il numero di software
    # installati nel relativo sotto-albero considerando
    # tale figlio (root del sotto-albero) con il software installato
    # se l'indice è 1 (best[c][1]), oppure senza consideralo
    # installato su di esso (best[c][0])

    for c in tree.children(root):
        best[c][False], best[c][True] = bacefook_algorithm(tree, c, best)

    withoutRoot = sum(best[c][True] for c in tree.children(root))
    withRoot = 1 + sum(min(best[c][False], best[c][True]) for c in tree.children(root))
    return withoutRoot, withRoot


def bacefook_minimum_softwares(tree: GeneralTree):
    best = {i: {False: 0, True: 0} for i in tree.postorder()}
    best[tree.root()][False], best[tree.root()][True] = bacefook_algorithm(tree, tree.root(), best)
    return best


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

    print(bacefook_minimum_softwares(tree))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time() - start_time)
