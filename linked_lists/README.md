# Singly Linked Lists

A singly linked list is the simplest type of linked list. Each node contains data and a reference (or "pointer") to the next node in the sequence.

A node can be represented as a simple class:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

The linked list itself is a class that holds a reference to the `head` of the list.

## Time Complexity of Singly Linked List Operations

| Operation                  | Big O | Notes                                                                   |
|----------------------------|-------|-------------------------------------------------------------------------|
| Access (by index)          | O(n)  | Requires traversing from the head.                                      |
| Search (by value)          | O(n)  | Requires traversing from the head.                                      |
| Insertion (at beginning)   | O(1)  | Just need to update the head.                                           |
| Insertion (at end)         | O(n)  | Requires traversing to the last node to update its `next` pointer.      |
| Deletion (at beginning)    | O(1)  | Just need to update the head.                                           |
| Deletion (at end or middle)| O(n)  | Requires traversing to the node *before* the one to be deleted.         |

Singly linked lists are efficient for use cases where you need fast insertions and deletions at the beginning of the sequence (like implementing a stack). However, they are slow for random access. 