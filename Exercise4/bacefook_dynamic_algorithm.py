from Exercise4.n_tree import NTree


def bacefook_minimum_softwares(tree: NTree, root: NTree.Position, tab):
    """
        method to compute the minimum number of user with software"""

    for c in tree.children(root):
        tab[c][True], tab[c][False] = bacefook_minimum_softwares(tree, c, tab)

    yes_software = sum(min(tab[c][False], tab[c][True]) for c in tree.children(root))
    no_software = sum(tab[c][True] for c in tree.children(root))
    return yes_software + 1, no_software


def bacefook_dynamic_algorithm(tree: NTree):
    """
        create a dict to store the number of subtree with or without the software

        tab dictionary structure:
        -Key i represents a node of the N Tree
        -Value is a dict in which we store the number of nodes in the subtree of the keys
         that have the software (With the software on the node-key or without [True or False])

    """

    tab = {i: {True: 0, False: 0} for i in tree.preorder()}
    tab[tree.root()][True], tab[tree.root()][False] = bacefook_minimum_softwares(tree, tree.root(), tab)
    return tab
