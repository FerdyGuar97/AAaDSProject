from Exercise4.general_tree import GeneralTree


def bacefook_minimum_softwares(tree: GeneralTree, root: GeneralTree.Position, best):
    # La tabella deve essere intepretata come segue:
    # Ogni colonna rappresenta un nodo figlio di root,
    # ed in ogni cella è contenuto il numero di software
    # installati nel relativo sotto-albero considerando
    # tale figlio (root del sotto-albero) con il software installato
    # se l'indice è 1 (best[c][1]), oppure senza consideralo
    # installato su di esso (best[c][0])

    for c in tree.children(root):
        best[c][True], best[c][False] = bacefook_minimum_softwares(tree, c, best)

    yes_software = sum(min(best[c][False], best[c][True]) for c in tree.children(root))
    no_software = sum(best[c][True] for c in tree.children(root))
    return yes_software + 1, no_software


def bacefook_dynamic_algorithm(tree: GeneralTree):
    best = {i: {True: 0, False: 0} for i in tree.preorder()}
    best[tree.root()][True], best[tree.root()][False] = bacefook_minimum_softwares(tree, tree.root(), best)
    return best
