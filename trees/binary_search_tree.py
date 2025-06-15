# trees/binary_search_tree.py

class TreeNode:
    """A node in a Binary Search Tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """A class representing a Binary Search Tree."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Public method to insert a key."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        # If key is equal, do nothing to avoid duplicates
        return node

    def search(self, key):
        """Public method to search for a key."""
        return self._search_recursive(self.root, key) is not None

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)
        
    def delete(self, key):
        """Public method to delete a key."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else: # Node to be deleted is found
            # Case 1: Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Case 2: Node with two children
            # Get the in-order successor (smallest in the right subtree)
            temp = self._get_min_value_node(node.right)
            node.key = temp.key # Copy the successor's content to this node
            node.right = self._delete_recursive(node.right, temp.key) # Delete the successor
            
        return node

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """Returns a list of keys in ascending order."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

def main():
    bst = BinarySearchTree()
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)

    print(f"In-order traversal: {bst.inorder_traversal()}")
    print(f"Search for 40: {bst.search(40)}")
    print(f"Search for 90: {bst.search(90)}")
    print("-" * 20)
    
    print("Deleting 20 (leaf node)...")
    bst.delete(20)
    print(f"In-order traversal: {bst.inorder_traversal()}")
    
    print("Deleting 30 (node with one child)...")
    bst.insert(35) # To make 40 have one child
    bst.delete(40)
    print(f"In-order traversal: {bst.inorder_traversal()}")

    print("Deleting 50 (root node with two children)...")
    bst.delete(50)
    print(f"In-order traversal: {bst.inorder_traversal()}")
    print(f"New root should be 60: {bst.root.key == 60}")
    print("-" * 20)

if __name__ == "__main__":
    main() 