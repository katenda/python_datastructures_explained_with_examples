# Doubly Linked Lists

A doubly linked list is a type of linked list where each node contains data, a pointer to the next node, and a pointer to the previous node. This structure allows for traversal in both directions.

A node in a doubly linked list can be represented as follows:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

The list itself maintains pointers to both the `head` and the `tail` to enable efficient operations at both ends.

## Time Complexity of Doubly Linked List Operations

| Operation                  | Big O | Notes                                                                                    |
|----------------------------|-------|------------------------------------------------------------------------------------------|
| Access (by index)          | O(n)  | Requires traversing from the head (or tail, if optimized).                               |
| Search (by value)          | O(n)  | Requires traversing from the head.                                                       |
| Insertion (at beginning)   | O(1)  | Update `head` and `prev`/`next` pointers.                                                |
| Insertion (at end)         | O(1)  | Update `tail` and `prev`/`next` pointers. (An advantage over singly linked lists).       |
| Deletion (at beginning)    | O(1)  | Update `head`.                                                                           |
| Deletion (at end)          | O(1)  | Update `tail`.                                                                           |
| Deletion (given a node)    | O(1)  | No need to find the previous node; it's directly accessible. (A key advantage).          |

Doubly linked lists are more memory-intensive due to the extra `prev` pointer, but they offer significant performance benefits for certain operations, making them useful for implementing data structures like LRU caches, queues, and deques. 