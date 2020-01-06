from Exercise4.n_tree import NTree


def bacefook_minimum_softwares(tree: NTree, root: NTree.Position, tab):
    # La tabella deve essere intepretata come segue:
    # Ogni colonna rappresenta un nodo figlio di root,
    # ed in ogni cella è contenuto il numero di software
    # installati nel relativo sotto-albero considerando
    # tale figlio (root del sotto-albero) con il software installato
    # se l'indice è 1 (tab[c][1]), oppure senza consideralo
    # installato su di esso (tab[c][0])

    for c in tree.children(root):
        tab[c][True], tab[c][False] = bacefook_minimum_softwares(tree, c, tab)

    yes_software = sum(min(tab[c][False], tab[c][True]) for c in tree.children(root))
    no_software = sum(tab[c][True] for c in tree.children(root))
    return yes_software + 1, no_software


def bacefook_dynamic_algorithm(tree: NTree):
    tab = {i: {True: 0, False: 0} for i in tree.preorder()}
    tab[tree.root()][True], tab[tree.root()][False] = bacefook_minimum_softwares(tree, tree.root(), tab)
    return tab
