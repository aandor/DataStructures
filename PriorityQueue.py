class PriorityQueue:
    """Implements a priority queue using a binary heap."""
    
    def __init__(self):
        """Initialize an empty priority queue."""
        self.queue = []

    def __str__(self):
        """Return a string representation of the priority queue."""
        return str([f"{val} (Priority: {priority})" for priority, val in sorted(self.queue)])

    def push(self, val, priority):
        """Add an element to the queue with a given priority."""
        self.queue.append((priority, val))
        self._heapify_up(len(self.queue) - 1)

    def pop(self):
        """Remove and return the element with the highest priority (lowest priority number)."""
        if not self.queue:
            return None
        val = self.queue[0][1]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self._heapify_down(0)
        return val

    def _heapify_up(self, index):
        """Heapify upwards starting from a given index."""
        parent = (index - 1) // 2
        if parent >= 0 and self.queue[parent][0] > self.queue[index][0]:
            self.queue[parent], self.queue[index] = self.queue[index], self.queue[parent]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """Heapify downwards starting from a given index."""
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < len(self.queue) and self.queue[left][0] < self.queue[smallest][0]:
            smallest = left
        if right < len(self.queue) and self.queue[right][0] < self.queue[smallest][0]:
            smallest = right
        if smallest != index:
            self.queue[smallest], self.queue[index] = self.queue[index], self.queue[smallest]
            self._heapify_down(smallest)

# Test cases
pq = PriorityQueue()
pq.push("medium", 1)
pq.push("high", 0)
pq.push("low", 2)
print("Priority Queue:", pq)
assert pq.pop() == "high"
assert pq.pop() == "medium"
assert pq.pop() == "low"
assert pq.pop() == None
