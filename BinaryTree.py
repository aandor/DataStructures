class Node:
    """Represents an individual node in the BST."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation."""
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def insert(self, value):
        """Public method to insert a value into the BST."""
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        """Helper method for insert operation."""
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def delete(self, value):
        """Public method to delete a value from the BST."""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        """Helper method for delete operation."""
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            min_larger_node = self._get_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value)
        return node

    def _get_min(self, node):
        """Helper method to find minimum value node in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, value):
        """Public method to search a value in the BST."""
        return self._search(self.root, value)

    def _search(self, node, value):
        """Helper method for search operation."""
        if node is None:
            return None
        if value < node.value:
            return self._search(node.left, value)
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return node

    def inorder_traversal(self):
        """Public method for in-order traversal of the BST."""
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, values):
        """Helper method for in-order traversal."""
        if node:
            self._inorder_traversal(node.left, values)
            values.append(node.value)
            self._inorder_traversal(node.right, values)
        return values

    def is_empty(self):
        """Check if the BST is empty."""
        return self.root is None

    def size(self):
        """Return the number of nodes in the BST."""
        return self._size(self.root)

    def _size(self, node):
        """Helper method to calculate the size of a subtree."""
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)


# Test the BinarySearchTree class
bst = BinarySearchTree()

# Test is_empty method on an empty tree
assert bst.is_empty() == True

# Test size method on an empty tree
assert bst.size() == 0

# Test insert method
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)

# Test is_empty method after insertion
assert bst.is_empty() == False

# Test size method after insertion
assert bst.size() == 5

# Test inorder_traversal method
assert bst.inorder_traversal() == [2, 5, 7, 10, 15]

# Test search method
assert bst.search(10).value == 10
assert bst.search(100) == None

# Test delete method
bst.delete(2)
bst.delete(15)
assert bst.inorder_traversal() == [5, 7, 10]

# Test size method after deletion
assert bst.size() == 3

print("All test cases passed!")