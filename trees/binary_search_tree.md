# Binary Search Trees (BST)

A Binary Search Tree is a node-based binary tree data structure which has the following properties:

*   The left subtree of a node contains only nodes with keys lesser than the node's key.
*   The right subtree of a node contains only nodes with keys greater than the node's key.
*   The left and right subtree each must also be a binary search tree.
*   There must be no duplicate nodes.

This property allows for dictionary-like operations (search, insert, delete) to be performed very efficiently.

## Time Complexity of BST Operations

The efficiency of BST operations depends heavily on the **height (h)** of the tree.

| Operation | Average Case (Balanced) | Worst Case (Unbalanced) |
|-----------|-------------------------|-------------------------|
| Search    | O(log n)                | O(n)                    |
| Insert    | O(log n)                | O(n)                    |
| Delete    | O(log n)                | O(n)                    |

A **balanced** tree is one where the height is minimized, roughly `log n`. An **unbalanced** tree is skewed, with a height that can be as large as `n`, effectively turning it into a linked list. This is why self-balancing trees like AVL trees exist, which we will cover later.

## In-order Traversal of a BST

A key feature of a BST is that an **in-order traversal** (`Left -> Root -> Right`) visits the nodes in ascending sorted order. This is a useful property for many algorithms and for verifying that the tree is structured correctly. 