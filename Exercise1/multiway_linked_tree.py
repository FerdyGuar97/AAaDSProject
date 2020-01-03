from Exercise1.multiway_tree import MultiwayTree


class MultiwayLinkedTree(MultiwayTree):
    # -------------------------- nested Node class --------------------------
    class _Node:
        """An abstraction representing a node containing more tha one element"""
        __slots__ = '_parent', '_children', '_elements'

        def __init__(self, elements, parent=None, children=None):
            self._parent = parent
            self._elements = elements
            self._children = children

        def _split(self):
            """The node splits itself in two nodes and returns a tuple containing
            those two nodes and the central element.
            (n1 , e , n2) <- return tuple
            """
            raise NotImplementedError("must be implemented by subclass")

    # -------------------------- nested Position class --------------------------
    class Position(MultiwayTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node, index):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
            self._index = index

        def element(self):
            """Return the element stored at this Position."""
            return self._node._elements[self._index]

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node and other._index == self._index

    # -------------------------- multiway alberi constructor --------------------------
    def __init__(self):
        """Create an initially empty multiway alberi."""
        self._root = None
        self._size = 0

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent, 0)

    def num_children(self, p):
        """Return the number of children of Position p."""
        return len(p._node._children)

    # ------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        if p._index < 0 or p._index >= len(p._node._children):
            raise ValueError('p\'s index out of bound')
        return (p._node, p._index)

    def _make_position(self, node, index):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node, index) if node is not None else None

    # -------------------------- nonpublic mutators --------------------------
    def _add_root(self, e):
        """Place element e at the root of an empty alberi and return new Position.

        Raise ValueError if alberi nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node([e])
        return self._make_position(self._root, 0)

    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node, index = self._validate(p)
        old = node._elements[index]
        node._elements[index] = e
        return old

    def __len__(self):
        return self._size

    def _add_before(self, p, e):
        """Create a new child before Position p, storing e as first element.

        Return the Position of new element.
        Raise ValueError if Position p is invalid or p already has a child before p.
        """
        node, index = self._validate(p)
        if node._children[index] is not None:
            raise ValueError('Child with index ' + str(index) + ' exists')
        self._size += 1
        node._children[index] = self._Node([e], node)  # node is its parent
        return self._make_position(node._children[index], 0)

    def _add_after(self, p, e):
        """Create a new child after Position p, storing e as first element.

        Return the Position of new element.
        Raise ValueError if Position p is invalid or p already has a child after p.
        """
        node, index = self._validate(p)
        index += 1
        if node._children[index] is not None:
            raise ValueError('Child with index ' + str(index) + ' exists')
        self._size += 1
        node._children[index] = self._Node([e], node)  # node is its parent
        return self._make_position(node._children[index], 0)