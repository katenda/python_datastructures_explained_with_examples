# graphs/graph_traversals.py
from collections import deque, defaultdict

class Graph:
    """
    A class to represent a graph using an adjacency list.
    """
    def __init__(self):
        # Use a defaultdict to easily handle adding edges for new vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        """Adds an edge to an undirected graph."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start_node):
        """
        Performs Depth-First Search traversal starting from a given node.

        Approach:
        Uses recursion (and the implicit call stack) to explore as deeply
        as possible down one branch before backtracking. A `visited` set is
        crucial to avoid infinite loops in graphs with cycles.
        """
        print("--- Depth-First Search (DFS) ---")
        visited = set()
        result = []
        self._dfs_recursive(start_node, visited, result)
        print("Path:", " -> ".join(result))
        return result

    def _dfs_recursive(self, node, visited, result):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in self.adj_list[node]:
                self._dfs_recursive(neighbor, visited, result)

    def bfs(self, start_node):
        """
        Performs Breadth-First Search traversal starting from a given node.

        Approach:
        Uses a queue to explore nodes level by level. A `visited` set is
        used to keep track of nodes already enqueued to avoid reprocessing
        and infinite loops.
        """
        print("--- Breadth-First Search (BFS) ---")
        visited = {start_node}
        queue = deque([start_node])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        print("Path:", " -> ".join(result))
        return result

def main():
    # Create a graph
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'F')
    
    #        A
    #       / \\
    #      B   C
    #     / \\ /
    #    D   E-F

    print("Graph Structure:", dict(g.adj_list))
    print("")

    # Perform DFS
    g.dfs('A')
    # Possible Output: A -> B -> D -> E -> F -> C
    print("")

    # Perform BFS
    g.bfs('A')
    # Output: A -> B -> C -> D -> E -> F
    print("")


if __name__ == "__main__":
    main() 