# linked_lists/doubly_linked_list.py

class Node:
    """A node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """A class representing a doubly linked list."""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Appends a new node to the end of the list.
        Time Complexity: O(1) because we use a tail pointer.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        """
        Prepends a new node to the beginning of the list.
        Time Complexity: O(1).
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, key):
        """Deletes a node with the given key."""
        current = self.head
        while current:
            if current.data == key:
                # If it's not the head, update the previous node's next pointer
                if current.prev:
                    current.prev.next = current.next
                else: # It is the head
                    self.head = current.next
                
                # If it's not the tail, update the next node's prev pointer
                if current.next:
                    current.next.prev = current.prev
                else: # It is the tail
                    self.tail = current.prev
                
                # We can stop after finding and deleting the first occurrence
                return
            current = current.next

    def display_forward(self):
        """Displays the list from head to tail."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Forward: " + " <-> ".join(elements))

    def display_backward(self):
        """Displays the list from tail to head."""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        print("Backward: " + " <-> ".join(elements))


def main():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    
    print("Initial list:")
    dll.display_forward()
    dll.display_backward()
    print("-" * 20)
    
    dll.prepend(0)
    print("After prepending 0:")
    dll.display_forward()
    dll.display_backward()
    print("-" * 20)

    dll.delete(2)
    print("After deleting 2:")
    dll.display_forward()
    dll.display_backward()
    print("-" * 20)

    dll.delete(0) # Delete head
    print("After deleting head (0):")
    dll.display_forward()
    dll.display_backward()
    print("-" * 20)
    
    dll.delete(3) # Delete tail
    print("After deleting tail (3):")
    dll.display_forward()
    dll.display_backward()
    print("-" * 20)

if __name__ == "__main__":
    main() 