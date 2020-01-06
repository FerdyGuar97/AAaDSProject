from Exercise1.multiway_linked_tree import ABTree


def main():
    tree = ABTree(2, 4)
    tree.add('b')
    tree.add('a')
    tree.add('e')
    tree.add('f')
    for p in tree.preorder():
        print(p._node._elements)


if __name__ == '__main__':
    main()
