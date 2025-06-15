from collections import deque, defaultdict

# --- Problem 1: Number of Connected Components ---

def number_of_connected_components(n: int, edges: list[list[int]]) -> int:
    """
    Problem: You have a graph of n nodes. You are given an integer n and an
    array edges where edges[i] = [ai, bi] indicates that there is an edge
    between ai and bi in the graph. Return the number of connected components.

    Approach:
    1. Build an adjacency list representation of the graph.
    2. Create a `visited` set to keep track of visited nodes.
    3. Initialize a `count` of components to 0.
    4. Iterate from node 0 to n-1. If a node has not been visited, it means
       we've found a new component. Increment the count and start a traversal
       (DFS or BFS) from this node to find all nodes in its component and
       mark them as visited.
    5. Return the final count.
    """
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    visited = set()
    count = 0
    
    for i in range(n):
        if i not in visited:
            count += 1
            # Start a traversal (DFS chosen here)
            stack = [i]
            visited.add(i)
            while stack:
                node = stack.pop()
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
    return count

# --- Problem 2: Clone Graph ---

class Node:
    """Node for the Clone Graph problem."""
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: 'Node') -> 'Node':
    """
    Problem: Given a reference to a node in a connected undirected graph,
    return a deep copy of the graph.

    Approach:
    Use a hash map to store a mapping from original nodes to their copies.
    This map serves two purposes:
    1. It acts as a `visited` set to avoid infinite loops.
    2. It allows us to retrieve already created clones to connect edges.
    We can use either BFS or DFS to traverse the original graph.

    Time/Space Complexity: O(V + E) where V is vertices, E is edges.
    """
    if not node:
        return None
        
    old_to_new = {}
    
    def dfs_clone(original_node):
        if original_node in old_to_new:
            return old_to_new[original_node]
        
        copy_node = Node(original_node.val)
        old_to_new[original_node] = copy_node
        
        for neighbor in original_node.neighbors:
            copy_node.neighbors.append(dfs_clone(neighbor))
            
        return copy_node

    return dfs_clone(node)

# --- Problem 3: Course Schedule ---

def can_finish_courses(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    Problem: Can you finish all courses given a list of prerequisites?
    This is equivalent to detecting a cycle in a directed graph.

    Approach:
    Use DFS with cycle detection. We need to track the state of each node:
    - `unvisited`: We haven't explored this node yet.
    - `visiting`: We are currently in the recursion stack for this node.
    - `visited`: We have finished exploring this node and its neighbors.

    If our DFS encounters a node that is currently in the `visiting` state,
    we have found a back edge, which means there is a cycle.
    """
    adj_list = defaultdict(list)
    for course, prereq in prerequisites:
        adj_list[course].append(prereq)
    
    # Track states: 0=unvisited, 1=visiting, 2=visited
    visit_state = [0] * num_courses
    
    def has_cycle(course):
        visit_state[course] = 1 # Mark as visiting
        
        for prereq in adj_list[course]:
            if visit_state[prereq] == 1: # Cycle detected
                return True
            if visit_state[prereq] == 0:
                if has_cycle(prereq):
                    return True
        
        visit_state[course] = 2 # Mark as visited
        return False

    for i in range(num_courses):
        if visit_state[i] == 0:
            if has_cycle(i):
                return False
                
    return True


def main():
    print("--- Number of Connected Components ---")
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(f"For n={n} and edges={edges}, components = {number_of_connected_components(n, edges)}")
    print("-" * 20)

    print("--- Clone Graph ---")
    # For demonstration, we'd need to build a graph of Node objects.
    # This problem is more about the logic than the setup.
    print("Clone Graph logic is implemented. Setup is non-trivial for a simple demo.")
    print("-" * 20)

    print("--- Course Schedule ---")
    num_courses = 2
    prerequisites = [[1, 0]]
    print(f"Can finish {num_courses} courses with prereqs {prerequisites}? {can_finish_courses(num_courses, prerequisites)}")

    num_courses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(f"Can finish {num_courses} courses with prereqs {prerequisites}? {can_finish_courses(num_courses, prerequisites)}")
    print("-" * 20)


if __name__ == "__main__":
    main() 