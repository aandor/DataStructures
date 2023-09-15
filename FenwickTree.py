class FenwickTree:
    def __init__(self, arr):
        """Initialize a Fenwick Tree with an array."""
        self.array_size = len(arr)
        self.tree = [0] * (self.array_size + 1)
        self.construct_tree(arr)

    def construct_tree(self, arr):
        """Construct the Fenwick Tree using the given array."""
        for index in range(self.array_size):
            self.update_tree(index, arr[index])

    def update_tree(self, index, value):
        """Update the Fenwick Tree at a given index with a value."""
        index += 1
        while index <= self.array_size:
            self.tree[index] += value
            index += index & -index

    def query_sum(self, index):
        """Query the sum from index 0 to the given index."""
        if self.array_size == 0:
            return 0
        index += 1
        total_sum = 0
        while index > 0:
            total_sum += self.tree[index]
            index -= index & -index
        return total_sum

# Test cases

test_array = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
fenwick_tree = FenwickTree(test_array)
assert fenwick_tree.query_sum(5) == 12  # Sum from index 0 to 5
assert fenwick_tree.query_sum(0) == 2  # Sum at index 0 should be the element itself

# Update element at index 3 and test again
fenwick_tree.update_tree(3, 6)
assert fenwick_tree.query_sum(5) == 18  # Sum from index 0 to 5 after update

# Test with negative numbers
negative_array = [-1, -2, -3, -4]
negative_tree = FenwickTree(negative_array)
assert negative_tree.query_sum(2) == -6  # Sum from index 0 to 2

# Test with single-element array
single_element_array = [5]
single_element_tree = FenwickTree(single_element_array)
assert single_element_tree.query_sum(0) == 5  # Sum at index 0 should be the element itself

# Test with empty array
empty_array = []
empty_tree = FenwickTree(empty_array)
assert empty_tree.query_sum(0) == 0  # Sum at index 0 should be 0 for an empty array

print("All tests passed!")