class Node:
    """A class to represent a node in a singly linked list."""
    
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """A class to represent a singly linked list."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after(self, prev_data, new_data):
        """Insert a new node after a specific node."""
        prev_node = self.find(prev_data)
        if prev_node is None:
            print("Node not found.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, data):
        """Delete a node by its data."""
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next

    def find(self, data):
        """Find a node by its data."""
        temp = self.head
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next
        return None

    def size(self):
        """Get the size of the list."""
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def print_list(self):
        """Print the elements of the list."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):
        """Reverse the list in-place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_nth(self, n):
        """Get the nth element in the list."""
        count = 0
        temp = self.head
        while temp:
            if count == n:
                return temp.data
            count += 1
            temp = temp.next
        return None


# Test cases

def test_singly_linked_list():
    # Initialize list
    ll = SinglyLinkedList()
    
    # Test is_empty
    assert ll.is_empty() == True
    
    # Test insert_beginning
    ll.insert_beginning(1)
    assert ll.get_nth(0) == 1
    
    # Test insert_end
    ll.insert_end(2)
    assert ll.get_nth(1) == 2
    
    # Test insert_after
    ll.insert_after(1, 1.5)
    assert ll.get_nth(1) == 1.5
    
    # Test delete_node
    ll.delete_node(1.5)
    assert ll.find(1.5) == None
    
    # Test find
    assert ll.find(1).data == 1
    assert ll.find(5) == None
    
    # Test size
    assert ll.size() == 2
    
    # Test reverse
    ll.reverse()
    assert ll.get_nth(0) == 2
    assert ll.get_nth(1) == 1
    
    # Test get_nth
    assert ll.get_nth(0) == 2
    assert ll.get_nth(2) == None
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_singly_linked_list()
