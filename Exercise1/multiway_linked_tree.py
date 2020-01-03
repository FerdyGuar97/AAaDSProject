from Exercise1.multiway_tree import MultiwayTree

class MultiwayLinkedTree(MultiwayTree):

    # -------------------------- nested Node class --------------------------
    class _Node:
        """An abstraction representing a node containing more tha one element"""
        __slots__ = '_parent'

        def __init__(self, parent, elements = None, children = None):
            self._parent = parent
            self._set_elements(elements)
            self._set_children(children)

        def _elements(self):
            raise NotImplementedError("must be implemented by subclass")

        def _children(self):
            raise NotImplementedError("must be implemented by subclass")

        def _set_elements(self,e):
            raise NotImplementedError("must be implemented by subclass")

        def _set_children(self,c):
            raise NotImplementedError("must be implemented by subclass")

    # -------------------------- nested Position class --------------------------
    class Position(MultiwayTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node, element):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
            self._element = element

        def element(self):
            """Return the element stored at this Position."""
            return self._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node and other._element == self._element

    # -------------------------- multiway alberi constructor --------------------------
    def __init__(self):
        """Create an initially empty multiway alberi."""
        self._root = None
        self._size = 0

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent,node._elements()[0])

    def num_children(self, p):
        """Return the number of children of Position p."""
        return len(p._node._children())

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

    def _make_position(self, node, element):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node,element) if node is not None else None