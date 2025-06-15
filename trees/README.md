# Binary Trees

A tree is a hierarchical data structure consisting of nodes connected by edges. A **binary tree** is a specific type of tree where each node can have at most two children: a `left` child and a `right` child.

## Key Terminology

*   **Node**: The fundamental part of a tree that stores data and links to its children. A simple Python representation is:
    ```python
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    ```
*   **Root**: The single topmost node in a tree.
*   **Parent**: A node that has one or more children.
*   **Child**: A node that has a parent.
*   **Leaf**: A node with no children.
*   **Subtree**: A tree consisting of a node and all of its descendants.

## Tree Traversal

Traversal is the process of visiting each node in a tree exactly once. Unlike linear data structures, trees can be traversed in multiple ways. The three most common methods are forms of Depth-First Search (DFS):

1.  **In-order Traversal**: Visits nodes in the order: `Left -> Root -> Right`. For a Binary Search Tree, this traversal visits nodes in ascending order.
2.  **Pre-order Traversal**: Visits nodes in the order: `Root -> Left -> Right`. This is useful for creating a copy of a tree.
3.  **Post-order Traversal**: Visits nodes in the order: `Left -> Right -> Root`. This is useful for deleting nodes from a tree, as you delete the children before the parent.

There is also a breadth-first traversal method:
4.  **Level-order Traversal**: Visits nodes level by level, from left to right. This is achieved using a queue and is also known as Breadth-First Search (BFS). 