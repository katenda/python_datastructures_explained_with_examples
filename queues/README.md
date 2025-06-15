# Queues

A queue is a linear data structure that operates on the **First-In, First-Out (FIFO)** principle. This means the first element added to the queue is the first one to be removed, just like a real-world queue or line.

## Core Operations

A queue supports the following primary operations, all of which should ideally have a time complexity of **O(1)**:

*   **`enqueue(item)`**: Adds an item to the back (end) of the queue.
*   **`dequeue()`**: Removes and returns the item from the front of the queue.
*   **`peek()`** (or `front`): Returns the front item without removing it.
*   **`is_empty()`**: Returns `True` if the queue is empty, `False` otherwise.
*   **`size()`**: Returns the number of items in the queue.

## Implementations in Python

### 1. Using `list` (Inefficient)

A Python `list` can be used to simulate a queue, but it is highly inefficient for this purpose.
*   `enqueue`: `list.append()` (This part is efficient, O(1) amortized).
*   `dequeue`: `list.pop(0)` (This is very slow, **O(n)**, because all subsequent elements must be shifted).

Using a list for a queue is generally discouraged in performance-critical code.

### 2. Using `collections.deque` (Recommended)

The `collections.deque` (double-ended queue) is specifically designed for fast appends and pops from both ends. It is the ideal choice for implementing a queue in Python.
*   `enqueue`: `deque.append()` (O(1) time complexity).
*   `dequeue`: `deque.popleft()` (O(1) time complexity).

This is the standard, performant way to create queues. 