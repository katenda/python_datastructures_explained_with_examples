# Dynamic Programming (DP)

Dynamic Programming is an algorithmic technique for solving optimization problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid redundant computation.

A problem must have two key properties to be solvable with DP:

1.  **Overlapping Subproblems**: The recursive solution involves solving the same subproblems multiple times.
2.  **Optimal Substructure**: The optimal solution to the overall problem can be constructed from the optimal solutions to its subproblems.

## Approaches to Dynamic Programming

### 1. Top-Down with Memoization

This approach is a "cached" version of recursion.
*   **Logic**: Write the solution recursively as you normally would.
*   **Optimization**: Store the result of each subproblem in a cache (e.g., a dictionary or an array). Before computing a solution, check the cache. If the result is already there, return it. Otherwise, compute it, store it in the cache, and then return it.
*   **Pros**: Often more intuitive to write as it closely follows the recursive formula.

### 2. Bottom-Up with Tabulation

This approach solves the problem iteratively.
*   **Logic**: Figure out the order in which subproblems need to be solved and build up the solution from the "bottom".
*   **Optimization**: You fill a table (e.g., a 1D or 2D array) with the results of subproblems, starting with the base cases. Each entry `dp[i]` is calculated based on previous entries.
*   **Pros**: Can be more space-efficient and avoids deep recursion stacks, preventing stack overflow errors.

## Example: Fibonacci Sequence

The Fibonacci sequence is the "hello world" of dynamic programming.
*   **Naive Recursion**: `fib(n) = fib(n-1) + fib(n-2)`. This has O(2^n) complexity due to re-computing the same values.
*   **DP (Memoization or Tabulation)**: By storing the results of `fib(k)`, we can reduce the complexity to **O(n)**. 