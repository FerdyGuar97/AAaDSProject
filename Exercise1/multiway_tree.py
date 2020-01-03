from TdP_collections.tree.tree import Tree


class MultiwayTree(Tree):
    """Abstract base class representing a multiway alberi structure."""

    def siblings(self, p):
        raise NotImplementedError("must be implemented by subclass")
