from Exercise1.BTree import BTree

def main():
    tree = BTree()
    tree.add('b')
    tree.add('a')
    tree.add('e')
    tree.add('f')
    for p in tree.preorder():
        print(p._node._elements)
    tree.delete('a')
    for p in tree.preorder():
        print(p._node._elements)


if __name__ == '__main__':
    main()
