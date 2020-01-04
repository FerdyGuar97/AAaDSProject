from random import Random

from Exercise4.general_tree import GeneralTree
from TdP_collections.tree.linked_binary_tree import LinkedBinaryTree


def algorithm(tree: LinkedBinaryTree, root: LinkedBinaryTree.Position):
    if root is None:
        return 0
    if tree.num_children(root) == 0 and tree.parent(root) is None:
        tree._replace(root, (root.element(), True))
        return 1
    elif tree.num_children(root) == 0 and tree.parent(root) is not None:
        tree._replace(root, (root.element(), False))
        return 0
    elif tree.num_children(root) > 0:
        acc = 0
        so = False
        acc += algorithm(tree, tree.left(root))
        acc += algorithm(tree, tree.right(root))
        if tree.left(root):
            print(tree.left(root).element())
            so = so or not tree.left(root).element()[1]
        if tree.right(root):
            print(tree.right(root).element())
            so = so or not tree.right(root).element()[1]
        # for c in tree.children(root):
        #     acc += algorithm(tree, c)
        #     if not c.element()[1]:
        #         so = True
        if so:
            tree._replace(root, (root.element(), True))
            return acc + 1
        else:
            return acc


def main():
    tree = LinkedBinaryTree()
    g = tree._add_root(6)
    c = tree._add_left(g, 1)
    b = tree._add_right(g, 2)
    f = tree._add_left(b, 4)
    h = tree._add_right(b, 7)
    a = tree._add_left(c, 3)
    d = tree._add_right(c, 5)
    z = tree._add_left(a, 12)
    y = tree._add_left(z, 18)

    print(algorithm(tree, g))


if __name__ == '__main__':
    main()
