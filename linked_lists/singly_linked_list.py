# linked_lists/singly_linked_list.py

class Node:
    """
    A node in a singly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    A class representing a singly linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the list.
        Time Complexity: O(n) because we need to traverse to the end.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """
        Prepends a new node with the given data to the beginning of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """
        Deletes the first occurrence of a node with the given key.
        Time Complexity: O(n) in the worst case (deleting the last element).
        """
        current_node = self.head
        
        # Case 1: The node to be deleted is the head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        # Case 2: The node is somewhere else in the list
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        # If the key was not found in the list
        if not current_node:
            return

        # Unlink the node from the list
        prev_node.next = current_node.next
        current_node = None

    def display(self):
        """
        Displays the contents of the linked list.
        """
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(elements))

def main():
    # Create a new singly linked list
    sll = SinglyLinkedList()

    # Append elements
    sll.append(1)
    sll.append(2)
    sll.append(3)
    print("After appending 1, 2, 3:")
    sll.display()  # Output: 1 -> 2 -> 3

    # Prepend an element
    sll.prepend(0)
    print("After prepending 0:")
    sll.display()  # Output: 0 -> 1 -> 2 -> 3

    # Delete an element
    sll.delete(2)
    print("After deleting 2:")
    sll.display()  # Output: 0 -> 1 -> 3
    
    # Delete the head
    sll.delete(0)
    print("After deleting head (0):")
    sll.display() # Output: 1 -> 3
    
    # Try to delete a non-existent element
    sll.delete(99)
    print("After attempting to delete 99:")
    sll.display() # Output: 1 -> 3

if __name__ == "__main__":
    main() 