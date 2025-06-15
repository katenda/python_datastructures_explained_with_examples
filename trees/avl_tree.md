# AVL Trees

An AVL tree is a self-balancing Binary Search Tree (BST) where the difference between the heights of the left and right subtrees of any node is at most one. This difference is called the **balance factor**.

**Balance Factor = height(left subtree) - height(right subtree)**

For any node in an AVL tree, the balance factor must be in the set `{-1, 0, 1}`.

This balancing property ensures that the height of the tree remains logarithmic with respect to the number of nodes (`h = O(log n)`). This guarantees that search, insertion, and deletion operations have a worst-case time complexity of **O(log n)**, which is a significant advantage over standard BSTs.

## Tree Rotations

To maintain its balance property, an AVL tree performs **rotations** after an insertion or deletion that causes a node's balance factor to become -2 or 2.

There are four types of imbalances that are corrected with rotations:

1.  **Left-Left (LL) Case**: The new node is inserted in the left subtree of the left child of the unbalanced node.
    *   **Fix**: A single **right rotation** on the unbalanced node.

2.  **Right-Right (RR) Case**: The new node is inserted in the right subtree of the right child.
    *   **Fix**: A single **left rotation** on the unbalanced node.

3.  **Left-Right (LR) Case**: The new node is inserted in the right subtree of the left child.
    *   **Fix**: A **left rotation** on the left child, followed by a **right rotation** on the unbalanced node.

4.  **Right-Left (RL) Case**: The new node is inserted in the left subtree of the right child.
    *   **Fix**: A **right rotation** on the right child, followed by a **left rotation** on the unbalanced node.

While more complex to implement than a standard BST, the performance guarantee of an AVL tree makes it valuable for applications where frequent lookups are needed and worst-case performance must be avoided. 