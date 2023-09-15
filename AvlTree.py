class Node:
    """Node class for AVL Tree."""
    def __init__(self, value):
        """Initialize Node with value, left, right, and height."""
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  

class AVLTree:
    """Class for AVL Tree."""
    def __init__(self):
        """Initialize AVL Tree with root as None."""
        self.root = None

    def insert(self, value):
        """Public method to insert value into AVL Tree."""
        if not self.root:
            self.root = Node(value)
        else:
            self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        """Insert a value into the AVL Tree, and balance the tree."""
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        return self._balance(node)

    def _balance(self, node):
        """Balance the tree rooted at node."""
        balance_factor = self._get_balance(node)

        if balance_factor > 1:
            if value < node.left.value:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        if balance_factor < -1:
            if value > node.right.value:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        """Left rotate the subtree rooted at z."""
        y = z.right
        z.right = y.left
        y.left = z

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        """Right rotate the subtree rooted at z."""
        y = z.left
        z.left = y.right
        y.right = z

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        """Get the height of a node."""
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        """Get the balance factor of a node."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def search(self, value):
        """Public method to search a value."""
        return self._search(self.root, value) is not None

    def _search(self, node, value):
        """Search for a value in the tree rooted at node."""
        if node is None:
            return None

        if value < node.value:
            return self._search(node.left, value)
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return node

    def inorder_traversal(self):
        """Public method for in-order traversal."""
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, values):
        """Perform an in-order traversal rooted at node."""
        if node:
            self._inorder_traversal(node.left, values)
            values.append(node.value)
            self._inorder_traversal(node.right, values)
        return values

    def preorder_traversal(self):
        """Public method for pre-order traversal."""
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, node, values):
        """Perform a pre-order traversal rooted at node."""
        if node:
            values.append(node.value)
            self._preorder_traversal(node.left, values)
            self._preorder_traversal(node.right, values)
        return values

    def postorder_traversal(self):
        """Public method for post-order traversal."""
        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, node, values):
        """Perform a post-order traversal rooted at node."""
        if node:
            self._postorder_traversal(node.left, values)
            self._postorder_traversal(node.right, values)
            values.append(node.value)
        return values
    
    
# Initialize AVL Tree
avl = AVLTree()

# Test search on empty tree
assert avl.search(5) == False

# Test insert and root property
avl.insert(5)
assert avl.root.value == 5

# Test search after one insert
assert avl.search(5) == True

# Test multiple inserts and balancing
avl.insert(2)
avl.insert(8)
avl.insert(1)
avl.insert(3)
assert avl.root.value == 5  # Root should still be 5

# Test search functionality
assert avl.search(5) == True
assert avl.search(3) == True
assert avl.search(8) == True
assert avl.search(10) == False  # Should be False, 10 is not inserted

# Test in-order traversal
assert avl.inorder_traversal() == [1, 2, 3, 5, 8]

# Test pre-order traversal
assert avl.preorder_traversal() == [5, 2, 1, 3, 8]

# Test post-order traversal
assert avl.postorder_traversal() == [1, 3, 2, 8, 5]

print("All test cases passed!")
