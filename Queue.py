from collections import deque

class Queue:
    def __init__(self, max_size=None):
        """Initialize a new Queue with an optional max size."""
        self.items = deque()
        self.max_size = max_size

    def enqueue(self, item):
        """Add an item to the queue. Check for fullness."""
        if self.max_size is None or len(self.items) < self.max_size:
            self.items.append(item)
        else:
            return "Queue is full"

    def dequeue(self):
        """Remove and return the first item. Check for emptiness."""
        if not self.is_empty():
            return self.items.popleft()
        else:
            return "Queue is empty"

    def peek(self):
        """Return the first item without removing it."""
        if self.items:
            return self.items[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        """Check if the queue is empty."""
        return not self.items

    def size(self):
        """Return the size of the queue."""
        return len(self.items)

    def clear(self):
        """Empty the queue."""
        self.items.clear()

    def contain(self, item):
        """Check if the queue contains a specific item."""
        return item in self.items

    def to_list(self):
        """Convert the queue to a list."""
        return list(self.items)

    def from_list(self, items):
        """Initialize the queue from a list."""
        if type(items) == list: 
            self.items.extend(items)
        else:
            self.items.append(items)

    def print_queue(self):
        """Return the queue as a list."""
        return list(self.items)


# Test cases

def test_queue():
    # Initialize queue
    q = Queue()
    
    # Test is_empty
    assert q.is_empty() == True
    
    # Test enqueue
    q.enqueue(1)
    assert q.peek() == 1
    
    # Test size
    assert q.size() == 1
    
    # Test contain
    assert q.contain(1) == True
    
    # Test dequeue
    assert q.dequeue() == 1
    assert q.dequeue() == "Queue is empty"
    
    # Test from_list and to_list
    q.from_list([2, 3, 4])
    assert q.to_list() == [2, 3, 4]
    
    # Test clear
    q.clear()
    assert q.is_empty() == True

    print("All test cases passed!")

if __name__ == "__main__":
    test_queue()
