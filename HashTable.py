# Update the HashTable class to include a check for the load factor in the resize method
class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table."""
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        """Calculate the hash index for a key."""
        return hash(key) % self.size

    def set(self, key, value):
        """Set a value for a key."""
        index = self.hash_func(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[index].append([key, value])
        
        # Check the load factor after each insertion
        if self.load_factor() > 0.7:
            self.resize()

    def get(self, key):
        """Get the value for a key."""
        index = self.hash_func(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def delete(self, key):
        """Delete a key-value pair."""
        index = self.hash_func(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return

    def resize(self):
        """Resize the hash table considering the load factor."""
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]
        for bucket in self.table:
            for key, value in bucket:
                index = hash(key) % new_size
                new_table[index].append([key, value])
        self.table = new_table
        self.size = new_size

    def contains(self, key):
        """Check if a key exists."""
        return self.get(key) is not None

    def keys(self):
        """Get all keys."""
        return [key for bucket in self.table for key, _ in bucket]

    def values(self):
        """Get all values."""
        return [value for bucket in self.table for _, value in bucket]

    def items(self):
        """Get all key-value pairs."""
        return [(key, value) for bucket in self.table for key, value in bucket]

    def load_factor(self):
        """Calculate the load factor."""
        return len(self.keys()) / self.size

    def clear(self):
        """Clear the hash table."""
        self.table = [[] for _ in range(self.size)]

    def __len__(self):
        """Get the number of items."""
        return len(self.keys())

    def __str__(self):
        """String representation."""
        return str(self.items())

    def __contains__(self, key):
        """Enable 'in' operator."""
        return self.contains(key)

    def __getitem__(self, key):
        """Enable bracket notation for getting items."""
        return self.get(key)

    def __setitem__(self, key, value):
        """Enable bracket notation for setting items."""
        self.set(key, value)

    def __delitem__(self, key):
        """Enable 'del' operator."""
        self.delete(key)


# Test cases for the HashTable class
ht = HashTable(size=5)  # Starting with a small size for easy testing of resize
# Test set and get
ht.set("a", 1)
assert ht.get("a") == 1
# Test delete
ht.delete("a")
assert ht.get("a") is None
# Test resize based on load factor
for i in range(5):
    ht.set(str(i), i)
assert ht.size == 10  # Should have resized
# Test contains
assert "4" in ht
# Test keys
assert set(ht.keys()) == set(map(str, range(5)))
# Test values
assert set(ht.values()) == set(range(5))
# Test items
assert set(ht.items()) == set((str(i), i) for i in range(5))
# Test load_factor
assert ht.load_factor() == 0.5  # 5 items in a size-10 table
# Test clear
ht.clear()
assert len(ht) == 0
# Test __getitem__, __setitem__, __delitem__
ht["c"] = 3
assert ht["c"] == 3
del ht["c"]
assert "c" not in ht

print("All test cases passed!")