from collections import deque

# --- Problem 1: Implement Stack using Queues ---

class MyStack:
    """
    Problem: Implement a LIFO stack using only two FIFO queues.

    Approach:
    We use two queues, q1 and q2. The `push` operation is the tricky part.
    To maintain LIFO order, the most recently pushed element must be at the
    front of our main queue.
    1. Add the new element to the empty queue (q2).
    2. Move all elements from the main queue (q1) to q2.
    3. Swap the names of q1 and q2.
    This way, the new element is at the front of q1, and the older elements
    are behind it, simulating a stack. `pop` and `top` then become simple
    operations on the front of q1.

    Time Complexity:
    - push: O(n) because we have to move all elements.
    - pop: O(1)
    - top: O(1)
    - empty: O(1)
    Space Complexity: O(n) to store the elements.
    """
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Add the new element to q1
        self.q1.append(x)
        # Move all elements back to q1
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1

# --- Problem 2: Binary Tree Level Order Traversal (BFS) ---

class TreeNode:
    """A simple node for a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: TreeNode) -> list[list[int]]:
    """
    Problem: Given the root of a binary tree, return the level order
    traversal of its nodes' values (i.e., from left to right, level by level).

    Approach:
    This is a classic Breadth-First Search (BFS) problem.
    1. Use a queue and initialize it with the root node.
    2. Loop as long as the queue is not empty.
    3. In each iteration, process all nodes currently in the queue (this constitutes one level).
    4. For each node, add its value to the current level's list and enqueue its children.
    5. Add the level's list to the final result.

    Time Complexity: O(n) because we visit each node exactly once.
    Space Complexity: O(w) where w is the maximum width of the tree. In the worst
    case (a complete binary tree), this is O(n).
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)

    return result

def main():
    print("--- Implement Stack using Queues ---")
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(f"Top of stack: {stack.top()}")   # returns 2
    print(f"Popped: {stack.pop()}")     # returns 2
    print(f"Is stack empty? {stack.empty()}") # returns false
    print("-" * 20)

    print("--- Binary Tree Level Order Traversal (BFS) ---")
    # Construct a sample tree:
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    traversal = level_order_traversal(root)
    print(f"Level order traversal: {traversal}")
    # Expected output: [[3], [9, 20], [15, 7]]
    print("-" * 20)

if __name__ == "__main__":
    main() 