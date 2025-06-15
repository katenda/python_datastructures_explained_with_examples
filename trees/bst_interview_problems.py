# trees/bst_interview_problems.py

class TreeNode:
    """A node in a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- Interview Problems ---

def is_valid_bst(root: TreeNode) -> bool:
    """
    Problem: Determine if a binary tree is a valid Binary Search Tree (BST).

    Approach:
    A naive check of `node.left.val < node.val < node.right.val` is insufficient.
    The entire left subtree must be less than the node, and the entire right
    subtree must be greater. We can solve this with a recursive traversal,
    passing down a valid range `(min_val, max_val)` for each node.
    A node is valid if its value is within this range. When we go left, we update
    the `max_val` to the current node's value. When we go right, we update the
    `min_val`.

    Time Complexity: O(n), as we visit each node once.
    Space Complexity: O(h), where h is the height of the tree, for the recursion stack.
    """
    def validate(node, low=-float('inf'), high=float('inf')):
        # An empty tree is a valid BST.
        if not node:
            return True
        
        # The current node's value must be within the valid range.
        if not (low < node.val < high):
            return False
        
        # Recursively check the left and right subtrees with updated ranges.
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root)

def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Problem: Find the Lowest Common Ancestor (LCA) of two given nodes in a BST.

    Approach:
    The BST property makes this very efficient. We start at the root.
    - If both p and q are smaller than the current node, the LCA must be in the left subtree.
    - If both p and q are larger than the current node, the LCA must be in the right subtree.
    - If one is smaller and one is larger (or one is the node itself), then the current
      node is the "split point" and is the LCA.

    Time Complexity: O(h), where h is the height of the tree.
    Space Complexity: O(1) for the iterative solution.
    """
    current = root
    while current:
        if p.val > current.val and q.val > current.val:
            current = current.right
        elif p.val < current.val and q.val < current.val:
            current = current.left
        else:
            # Found the split point, this is the LCA
            return current

def kth_smallest(root: TreeNode, k: int) -> int:
    """
    Problem: Find the k-th smallest element in a BST.

    Approach:
    An in-order traversal of a BST visits nodes in ascending sorted order.
    We can perform an iterative in-order traversal using a stack. We traverse
    as far left as possible, then process the nodes. We decrement `k` for each
    node we visit. When `k` reaches 0, the current node is our answer.

    Time Complexity: O(h + k), where h is the height. On average O(log n + k).
    Space Complexity: O(h) for the stack.
    """
    stack = []
    current = root
    
    while current or stack:
        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left
        
        # Process the node
        current = stack.pop()
        k -= 1
        if k == 0:
            return current.val
        
        # Move to the right subtree
        current = current.right

def main():
    print("--- Validate BST ---")
    # Valid BST
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Is tree [2,1,3] a valid BST? {is_valid_bst(root1)}")
    # Invalid BST
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(f"Is tree [5,1,4,null,null,3,6] a valid BST? {is_valid_bst(root2)}")
    print("-" * 20)

    print("--- Lowest Common Ancestor (LCA) of a BST ---")
    root = TreeNode(6)
    root.left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    root.right = TreeNode(8, TreeNode(7), TreeNode(9))
    p = root.left # Node 2
    q = root.right # Node 8
    lca = lowest_common_ancestor_bst(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {lca.val}") # Expected: 6
    
    p = root.left.right.left # Node 3
    q = root.left.right # Node 4
    lca = lowest_common_ancestor_bst(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {lca.val}") # Expected: 4
    print("-" * 20)
    
    print("--- Kth Smallest Element in a BST ---")
    root_k = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(f"For tree [3,1,4,null,2], the 1st smallest is: {kth_smallest(root_k, 1)}") # Expected: 1
    print(f"For tree [3,1,4,null,2], the 3rd smallest is: {kth_smallest(root_k, 3)}") # Expected: 3
    print("-" * 20)

if __name__ == "__main__":
    main() 