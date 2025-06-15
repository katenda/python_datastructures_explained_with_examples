# trees/avl_tree.py

import sys

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # Height of a new node is 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def insert(self, root, key):
        # 1. Perform standard BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get the balance factor
        balance = self.get_balance(root)

        # 4. If the node becomes unbalanced, then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        # 1. Perform standard BST delete
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self._get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # If the tree has only one node, simply return it
        if root is None:
            return root

        # 2. Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get the balance factor
        balance = self.get_balance(root)

        # 4. Rebalance the tree if needed
        # Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        # Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        # Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
        
    def pre_order(self, root):
        if not root:
            return []
        result = [root.key]
        result.extend(self.pre_order(root.left))
        result.extend(self.pre_order(root.right))
        return result

def main():
    my_tree = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = my_tree.insert(root, key)

    print("Pre-order traversal of the constructed AVL tree is:")
    print(my_tree.pre_order(root))
    # After inserting 10, 20, 30 -> 20 becomes root (RR case)
    # After inserting 40, 50 -> 30 rotates, 40 becomes root (RR case)
    # After inserting 25 -> RL case at node 20
    # Expected final tree pre-order: [30, 20, 10, 25, 40, 50]

    root = my_tree.delete(root, 10)
    
    print("\nPre-order traversal after deletion of 10:")
    print(my_tree.pre_order(root))
    # Expected final tree pre-order: [30, 20, 25, 40, 50]

if __name__ == "__main__":
    main() 