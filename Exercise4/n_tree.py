from TdP_collections.tree.tree import Tree


class NTree(Tree):
    class _Node:
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, element, parent=None, children=None):
            self._element = element
            self._children = children if children else []
            self._parent = parent

        def __hash__(self):
            return id(self)

        def __eq__(self, other):
            return other.__hash__() == self.__hash__()

        def __ne__(self, other):
            return not self == other

        def __repr__(self):
            print("{} -> Parent:{} num_children:{}".format(self._element,self._parent._element,len(self._children)))

    # -------------------------- nested Position class --------------------------
    class Position(Tree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __hash__(self):
            return self._node.__hash__()

        def __eq__(self, other):
            return other.__hash__() == self.__hash__()

        def __ne__(self, other):
            return not self == other

        def __repr__(self):
            return "{}".format(self.element())

    def __init__(self):
        self._root = None
        self._size = 0

    # ------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _attach_root(self, element):
        if self._root is not None:
            raise ValueError('this tree already has a root')
        self._root = self._Node(element)
        self._size += 1
        return self._make_position(self._root)

    def _attach_child(self, p, e):
        parent_node = self._validate(p)
        new_node = self._Node(e, parent_node)
        parent_node._children.append(new_node)
        # print("Now "+str(new_node._element)+" is a child of "+str(parent_node._element))
        self._size += 1
        return self._make_position(new_node)

    def add(self, e, p=None):
        if p is None:
            return self._attach_root(e)
        else:
            return self._attach_child(p, e)

    def replace(self, p, e):
        node = self._validate(p)
        old_e = node._element
        node._element = e
        return old_e

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        return self._make_position(p._node._parent)

    def num_children(self, p):
        return len(p._node._children)

    def children(self, p):
        self._validate(p)
        for c in p._node._children:
            if c is not None:
                yield self._make_position(c)

    def __len__(self):
        return self._size

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None
