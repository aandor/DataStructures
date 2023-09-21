class TrieNode:
    """Node class for a Trie."""
    def __init__(self):
        """Initialize Node with children and end of word marker."""
        self.children = {}
        self.is_end_of_word = False
        
class Trie:
    """Class for a Trie"""
    def __init__(self):
        """Initialize the Trie with root as a empty Node."""
        self.root = TrieNode()
        
    def insert(self, word):
        """Method to insert a value into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def search(self, word):
        """Method to search a value within the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
 
# Test cases 
    
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))     # Should return True
print(trie.search("app"))       # Should return False
trie.insert("app")
print(trie.search("apple"))     # Should return True
print(trie.search("app"))       # Should return True
print(trie.search("ap"))       # Should return False