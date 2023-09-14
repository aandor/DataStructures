class UnionFind:
    """Implements a Union-Find (Disjoint-Set) data structure for non-sequential and non-numeric elements."""
    
    def __init__(self, elements):
        """Initialize the Union-Find data structure."""
        self.map = {element: index for index, element in enumerate(elements)}
        self.parent = [i for i in range(len(elements))]
        self.rank = [0] * len(elements)
        self.size = [1] * len(elements)
        self.num_sets = len(elements)

    def _find(self, u):
        """Internal method to find the representative element of the set containing u."""
        if self.parent[u] == u:
            return u
        self.parent[u] = self._find(self.parent[u])
        return self.parent[u]

    def find(self, element):
        """Find the representative element of the set containing element."""
        return self._find(self.map[element])

    def union(self, u, v):
        """Merge the sets containing elements u and v."""
        u_index = self.map[u]
        v_index = self.map[v]
        u_root = self._find(u_index)
        v_root = self._find(v_index)

        if u_root == v_root:
            return

        if self.rank[u_root] > self.rank[v_root]:
            u_root, v_root = v_root, u_root

        self.parent[u_root] = v_root
        self.size[v_root] += self.size[u_root]

        if self.rank[u_root] == self.rank[v_root]:
            self.rank[v_root] += 1

        self.num_sets -= 1

    def elements_of_set(self, u):
        """Get all elements in the set containing u."""
        root = self._find(self.map[u])
        return [element for element, index in self.map.items() if self._find(index) == root]
    
    def is_same_set(self, u, v):
        """Check if elements u and v belong to the same set."""
        return self.find(u) == self.find(v)

    def size_of_set(self, u):
        """Get the size of the set containing element u."""
        return self.size[self.find(u)]

    def num_sets(self):
        """Get the number of disjoint sets."""
        return self.num_sets

    def reset(self):
        """Reset the Union-Find structure to its initial state."""
        self.parent = [i for i in range(len(self.parent))]
        self.rank = [0] * len(self.parent)
        self.size = [1] * len(self.parent)
        self.num_sets = len(self.parent)

# Initialize UnionFind with non-sequential and non-numeric elements
elements = ["A", "B", "C", "D", "E"]
uf = UnionFind(elements)

# Perform union operations
uf.union("A", "B")
uf.union("C", "D")

# Check if elements are in the same set and other utility methods
assert uf.is_same_set("A", "B") == True  # Should return True
assert uf.is_same_set("A", "C") == False  # Should return False
assert uf.size_of_set("A") == 2  # Should return 2
assert uf.elements_of_set("A") == ['A', 'B']  # Should return ['A', 'B']
uf.reset()
assert uf.is_same_set("A", "B") == False  # Should return False (since we reset)

print("All test cases passed!")
