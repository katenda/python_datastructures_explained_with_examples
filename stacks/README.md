# Stacks

A stack is a linear data structure that operates on the **Last-In, First-Out (LIFO)** principle. This means the last element added to the stack is the first one to be removed.

## Core Operations

A stack supports the following primary operations:

*   **`push(item)`**: Adds an item to the top of the stack.
*   **`pop()`**: Removes and returns the top item from the stack. If the stack is empty, this can raise an error.
*   **`peek()`** (or `top`): Returns the top item without removing it.
*   **`is_empty()`**: Returns `True` if the stack is empty, `False` otherwise.

All of these fundamental operations have a time complexity of **O(1)**, which makes stacks highly efficient for the specific problems they are designed to solve.

## Implementations in Python

### 1. Using `list`

Python's built-in `list` can be used as a stack.
*   `push` is implemented with `list.append()`.
*   `pop` is implemented with `list.pop()`.
*   `peek` is done by accessing the last element `my_list[-1]`.

While easy to use, `list` is a dynamic array. If it grows beyond its allocated memory, it needs to be reallocated, which can be a slow operation. For a very large number of push/pop operations, this can be a performance concern.

### 2. Using `collections.deque`

The `collections.deque` (double-ended queue) is the recommended way to implement a stack in Python. It is built on a doubly linked list, which provides O(1) time complexity for appends and pops from either end.
*   `push` is `deque.append()`.
*   `pop` is `deque.pop()`.

This is the more performant and robust option for implementing a stack. 