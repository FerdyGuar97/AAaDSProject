import sys

from Exercise4.general_tree import GeneralTree


def algorithm(tree: GeneralTree, root: GeneralTree.Position):
    if root is None:
        return 0
    elif tree.num_children(root) == 0 and tree.parent(root) is None:
        tree.replace(root, (root.element(), True))
        return 1
    elif tree.num_children(root) == 0 and tree.parent(root) is not None:
        tree.replace(root, (root.element(), False))
        return 0
    elif tree.num_children(root) > 0:
        acc = 0
        install_software = False
        # ------------ FOR LINKED BINARY TREE -------------
        # acc += algorithm(tree, tree.left(root))
        # acc += algorithm(tree, tree.right(root))
        # if tree.left(root):
        #     so = so or not tree.left(root).element()[1]
        # if tree.right(root):
        #     so = so or not tree.right(root).element()[1]
        for c in tree.children(root):
            acc += algorithm(tree, c)
            if not c.element()[1]:
                install_software = True

        if install_software:
            tree.replace(root, (root.element(), True))
            return acc + 1
        else:
            tree.replace(root, (root.element(), False))
            return acc


def main():
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

    print(algorithm(tree, a))

    for p in tree.preorder():
        print(p.element())

if __name__ == '__main__':
    main()
