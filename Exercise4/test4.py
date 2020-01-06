from Exercise4.bacefook_dynamic_algorithm import bacefook_dynamic_algorithm
from Exercise4.n_tree import NTree


def main():
    tree = NTree()
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

    map = bacefook_dynamic_algorithm(tree)
    string = ' '*len('False')
    true_string = 'True '
    false_string = 'False'
    for k in map:
        string += "| {} ".format(k)
    for k in map:
        true_string += "|{:3d}".format(map[k][True])
        false_string += "|{:3d}".format(map[k][False])


    print(string+"|")
    print(true_string+"|")
    print(false_string+"|")
    print("Minimum number of software: ",min(map[tree.root()].values()))



if __name__ == '__main__':
    main()
