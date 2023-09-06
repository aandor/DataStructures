class Node():
    """Class for creating a node for a doubly linked list."""
    
    def __init__(self, data):
        """Initialize node with data, next and previous pointers."""
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList():
    """Class for creating a doubly linked list."""
    
    def __init__(self):
        """Initialize an empty list with a head pointer."""
        self.head = None

    def find_node(self, data):
        """Find and return node containing data; return None if not found."""
        current = self.head
        while current:
            if (current.data == data):
                return current
            current = current.next
        return None

    def get_nth(self, data):
        """Return position of node containing data; return None if not found."""
        current_node = self.head
        count = 1
        while current_node:
            if current_node.data == data:
                return count
            current_node = current_node.next
            count += 1
        return None

    def insert_after(self, prev_node, data):
        """Insert node after a given node (prev_node)."""
        if (prev_node is None):
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

    def insert_beginning(self, data):
        """Insert node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        if (self.head is not None):
            self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        """Insert node at the end of the list."""
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def length(self):
        """Return the length of the list."""
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def print_list(self):
        """Print the list."""
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')

    def remove(self, data):
        """Remove a node containing data."""
        target_node = self.find_node(data)
        if not target_node:
            return
        prev_node, next_node = target_node.prev, target_node.next
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node
        if next_node:
            next_node.prev = prev_node
        del target_node

    def remove_duplicates(self):
        """Remove duplicate nodes from the list."""
        current_node = self.head
        seen = set()
        while current_node:
            next_node = current_node.next
            if current_node.data in seen:
                prev_node = current_node.prev
                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node
                if next_node:
                    next_node.prev = prev_node
                del current_node
            else:
                seen.add(current_node.data)
            current_node = next_node

    def reverse(self):
        """Reverse the list."""
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            current_node.prev = next_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def to_list(self):
        """Convert the list to a Python list."""
        lst = []
        current_node = self.head
        while current_node:
            lst.append(current_node.data)
            current_node = current_node.next
        return lst


# Test cases

def test_doubly_linked_list():
    # Create an empty list
    my_list = DoublyLinkedList()
    assert my_list.is_empty() == True

    # Test insert_beginning
    my_list.insert_beginning(5)
    my_list.insert_beginning(15)
    assert my_list.to_list() == [15, 5]
    assert my_list.is_empty() == False

    # Test insert_end
    my_list.insert_end(25)
    assert my_list.to_list() == [15, 5, 25]

    # Test insert_after
    my_list.insert_after(my_list.find_node(5), 20)
    assert my_list.to_list() == [15, 5, 20, 25]

    # Test find_node
    assert my_list.find_node(20).data == 20
    assert my_list.find_node(100) == None

    # Test get_nth
    assert my_list.get_nth(5) == 2
    assert my_list.get_nth(100) == None

    # Test length
    assert my_list.length() == 4

    # Test remove
    my_list.remove(15)
    assert my_list.to_list() == [5, 20, 25]

    # Test remove_duplicates
    my_list.insert_end(5)
    my_list.remove_duplicates()
    assert my_list.to_list() == [5, 20, 25]

    # Test reverse
    my_list.reverse()
    assert my_list.to_list() == [25, 20, 5]

    print("All test cases passed!")


if __name__ == "__main__":
    test_doubly_linked_list()
