# trees/binary_tree_traversals.py

class TreeNode:
    """A node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# --- Recursive Traversal Implementations ---

def inorder_traversal(root: TreeNode):
    """
    Performs an in-order traversal (Left, Root, Right).
    """
    if not root:
        return
    inorder_traversal(root.left)
    print(root.value, end=" ")
    inorder_traversal(root.right)

def preorder_traversal(root: TreeNode):
    """
    Performs a pre-order traversal (Root, Left, Right).
    """
    if not root:
        return
    print(root.value, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root: TreeNode):
    """
    Performs a post-order traversal (Left, Right, Root).
    """
    if not root:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value, end=" ")

def main():
    """
    Constructs the following tree for demonstration:
            F
           / \\
          B   G
         / \\   \\
        A   D   I
           / \\ /
          C  E H
    """
    root = TreeNode('F')
    root.left = TreeNode('B')
    root.right = TreeNode('G')
    root.left.left = TreeNode('A')
    root.left.right = TreeNode('D')
    root.left.right.left = TreeNode('C')
    root.left.right.right = TreeNode('E')
    root.right.right = TreeNode('I')
    root.right.right.left = TreeNode('H')

    print("--- Tree Traversals ---")
    
    print("In-order Traversal (Left, Root, Right):")
    inorder_traversal(root)
    print("\nExpected: A B C D E F G H I")
    print("-" * 30)

    print("Pre-order Traversal (Root, Left, Right):")
    preorder_traversal(root)
    print("\nExpected: F B A D C E G I H")
    print("-" * 30)

    print("Post-order Traversal (Left, Right, Root):")
    postorder_traversal(root)
    print("\nExpected: A C E D B H I G F")
    print("-" * 30)

if __name__ == "__main__":
    main() 