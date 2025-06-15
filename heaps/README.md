# Heaps

A heap is a specialized tree-based data structure that satisfies the heap property. It is also a **complete binary tree**, meaning all levels are filled except possibly the last one, which is filled from left to right.

This structure allows a heap to be efficiently implemented using an array.

## Heap Property

There are two main types of heaps, defined by the relationship between a parent and its children:

1.  **Min-Heap**: The key of a parent node is less than or equal to the keys of its children. The smallest element is always at the root.
2.  **Max-Heap**: The key of a parent node is greater than or equal to the keys of its children. The largest element is always at the root.

Because of this property, the primary use case for a heap is to implement a **Priority Queue**.

## Array-based Implementation

A heap can be represented as an array where the parent-child relationships are determined by index calculations:
*   For a node at index `i`:
    *   Left child is at `2*i + 1`
    *   Right child is at `2*i + 2`
    *   Parent is at `(i - 1) // 2`

## Time Complexity

The height of a complete binary tree with `n` nodes is `log n`. Heap operations involve "sifting" elements up or down the tree.

| Operation            | Big O    | Notes                                       |
|----------------------|----------|---------------------------------------------|
| Get Min/Max          | O(1)     | The root element is always the min/max.     |
| Extract Min/Max (pop)| O(log n) | Requires re-heapifying after removal.       |
| Insert (push)        | O(log n) | Requires re-heapifying after insertion.     |
| Build Heap           | O(n)     | Building a heap from an array of n items.   |

## Python's `heapq`

Python's standard library includes the `heapq` module, which provides an efficient implementation of a **min-heap**. This is the standard way to work with heaps in Python. 