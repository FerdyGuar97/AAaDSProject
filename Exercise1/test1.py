from Exercise1.BTree import BTree


def main():
    tree = BTree()
    tree[1] = 'b'
    tree[2] = 'a'
    tree[3] = 'e'
    tree[4] = 'f'
    for k in tree:
        print(tree[k])
    del tree[2]
    print()
    for k in tree:
        print(tree[k])


if __name__ == '__main__':
    main()
