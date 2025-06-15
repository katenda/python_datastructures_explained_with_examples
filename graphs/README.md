# Graphs

A graph is a non-linear data structure consisting of a finite set of **vertices** (or nodes) and a set of **edges** connecting them. Graphs are the ultimate data structure for modeling networks and relationships, from social networks to flight paths.

## Key Concepts

*   **Vertex**: An individual node in the graph.
*   **Edge**: A connection or link between two vertices.
*   **Undirected Graph**: Edges have no orientation. An edge `(A, B)` is the same as `(B, A)`.
*   **Directed Graph (Digraph)**: Edges have a direction. An edge `(A, B)` means there is a path from A to B, but not necessarily from B to A.
*   **Neighbor (or Adjacent Node)**: A vertex that is connected by an edge to another vertex.

## Graph Representation

There are two primary ways to represent a graph in code:

### 1. Adjacency List

This is the most common and generally most efficient method. An adjacency list is a dictionary (hash map) where each key is a vertex, and the value is a list (or set) of its neighbors.

**Example (Undirected Graph):**
A -- B
|    |
C -- D

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

*   **Pros**: Space-efficient for sparse graphs (where `Edges << Vertices^2`). Iterating over all of a vertex's neighbors is efficient.
*   **Cons**: Checking for a specific edge `(A, B)` takes O(degree(A)) time.

### 2. Adjacency Matrix

An adjacency matrix is a V x V matrix of booleans (or integers), where `V` is the number of vertices. The entry `matrix[i][j]` is `True` if an edge exists from vertex `i` to vertex `j`.

**Example (same graph):**
```
  A B C D
A 0 1 1 0
B 1 0 0 1
C 1 0 0 1
D 0 1 1 0
```

*   **Pros**: Checking for a specific edge `(A, B)` is very fast (O(1)).
*   **Cons**: Requires O(V^2) space, which is inefficient for sparse graphs. 