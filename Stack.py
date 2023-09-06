class Stack:
    def __init__(self, max_size=None):
        """Initialize a new stack. Can optionally provide max_size to limit stack size."""
        self.items = []
        self.max_size = max_size
    
    def is_empty(self):
        """Check if the stack is empty. Returns True if empty, otherwise False."""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)
    
    def pop(self):
        """Pop an item off the stack and return it. Returns None if the stack is empty."""
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        """Look at the item on the top of the stack without removing it. Returns None if the stack is empty."""
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def clear(self):
        """Remove all items from the stack."""
        self.items = []

    def contains(self, item):
        """Check if an item exists in the stack. Returns True if it does, otherwise False."""
        return item in self.items

    def to_list(self):
        """Return a list containing all items in the stack. The list is a copy."""
        return self.items.copy()

    def from_list(self, lst):
        """Replace all items in the stack with items from the given list. Truncates list to max_size if needed."""
        self.items = lst.copy()
        if self.max_size and len(self.items) > self.max_size:
            self.items = self.items[:self.max_size]

    def is_full(self):
        """Check if the stack is full. Returns True if full, otherwise False. Always returns False if max_size is None."""
        if self.max_size:
            return len(self.items) == self.max_size
        return False


# Test cases

def test_stack():
    # Initialize stack
    s = Stack(max_size=5)

    # Test is_empty
    assert s.is_empty() == True

    # Test push and pop
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2

    # Test peek
    s.push(4)
    assert s.peek() == 4

    # Test size
    assert s.size() == 2

    # Test clear
    s.clear()
    assert s.is_empty() == True

    # Test contains
    s.push(5)
    assert s.contains(5) == True

    # Test to_list
    assert s.to_list() == [5]

    # Test from_list
    s.from_list([1, 2, 3, 4, 5])
    assert s.to_list() == [1, 2, 3, 4, 5]

    # Test is_full
    assert s.is_full() == True

    print("All test cases passed!")


if __name__ == "__main__":
    test_stack()
