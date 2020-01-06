from array import array
from typing import _KT, _VT_co, _VT

from Exercise1.multiway_tree import MultiwayTree
from TdP_collections.hash_table.map_base import MapBase


class MultiwayLinkedTree(MultiwayTree, MapBase):
    def __setitem__(self, k: _KT, v: _VT) -> None:
        pass

    def __delitem__(self, v: _KT) -> None:
        pass

    def __getitem__(self, k: _KT) -> _VT_co:
        pass

    # -------------------------- nested Node class --------------------------
    class _Node:
        """An abstraction representing a node containing more tha one element"""
        __slots__ = '_parent', '_children', '_elements'

        def __init__(self, elements, parent=None, children=None):
            self._parent = parent
            self._elements = elements if elements else []
            self._children = children if children else []

        def _split(self):
            """The node splits itself in two nodes and returns a tuple containing
            those two nodes and the central element.
            (n1 , e , n2) <- return tuple
            """
            node1_end_index = len(self._elements) // 2 - 1
            node2_start_index = node1_end_index + 2

            node1 = self._Node(self._elements[:node1_end_index + 1], self._parent)
            node2 = self._Node(self._elements[node2_start_index:], self._parent)

            index_in_parent = None
            for i in range(0, len(self._parent._children)):
                if self == self._parent._children[i]:
                    index_in_parent = i;
            if index_in_parent is None:
                raise ValueError('Cannot find this node in its parent children')
            self._parent._elements.insert(index_in_parent, self._elements[node1_end_index + 1])

            self._parent._children.insert(index_in_parent, node1)
            self._parent._children.insert(index_in_parent + 1, node2)

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
        """Add an element in a node before Position p,
        doesn't perform any control on the max number of elements!

        Return the Position of new element.
        Raise ValueError if Position p is invalid or p already has a child before p.
        """
        node, index = self._validate(p)
        self._size += 1
        node._children.insert(index, e)
        return self._make_position(node, index)

    def _add_after(self, p, e):
        """Add an element in a node after Position p,
        doesn't perform any control on the max number of elements!

        Return the Position of new element.
        Raise ValueError if Position p is invalid or p already has a child before p.
        """
        node, index = self._validate(p)
        index += 1
        self._size += 1
        node._children.insert(index, e)
        return self._make_position(node, index)

    def _search(self, e, starting_vertex):
        """Search for an element in self tree.
        Return its Position or the Position in which it should be."""
        if starting_vertex is None:
            return None
        elif e > starting_vertex._elements[-1]:
            if starting_vertex._children[-1] is None:
                return self._make_position(starting_vertex, len(starting_vertex._elements))
            return self._search(e, starting_vertex._children[-1])
        elif e < starting_vertex._elements[0]:
            if starting_vertex._children[0] is None:
                return self._make_position(starting_vertex, 0)
            return self._search(e, starting_vertex._children[0])
        else:
            for i in range(0, len(self._elements)):
                if e <= self._elements[i]:
                    return self._make_position(starting_vertex, i)

    def _add(self, e):
        """Add an element in tree.
        Return its Position"""

        if self._root is None:
            self._add_root(e)
        else:
            e_position = self._search(e, self._root)
            if e == e_position.element():
                return e_position
            else:
                self._add_before(e_position, e)
