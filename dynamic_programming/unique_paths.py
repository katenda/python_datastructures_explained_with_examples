# dynamic_programming/unique_paths.py

# --- 1. Bottom-Up Dynamic Programming with Tabulation (2D) ---

def unique_paths_tabulation(m: int, n: int) -> int:
    """
    Solves the Unique Paths problem using a 2D DP table.
    dp[row][col] = the number of unique paths to reach that cell.

    Recurrence Relation:
    dp[row][col] = dp[row-1][col] (from above) + dp[row][col-1] (from left)

    Time Complexity: O(m * n)
    Space Complexity: O(m * n) for the dp table.
    """
    # Create an m x n grid initialized to 0
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Base cases: Fill the first row and first column with 1s
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
        
    # Fill the rest of the table using the recurrence relation
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    # The result is in the bottom-right corner
    return dp[m-1][n-1]

# --- 2. Bottom-Up DP with Space Optimization ---

def unique_paths_optimized(m: int, n: int) -> int:
    """
    This version optimizes space. To calculate the values for the current row,
    we only need the values from the previous row. We can use a single 1D array
    to represent the previous row and update it in place to calculate the current row.

    Time Complexity: O(m * n)
    Space Complexity: O(n) (the width of the grid)
    """
    # We use a single row as our DP table
    row = [1] * n
    
    # We iterate for m-1 rows (since the first row is already calculated as all 1s)
    for i in range(m - 1):
        # Create a new row based on the previous row
        new_row = [1] * n # The first element of every row is always 1
        for j in range(1, n):
            # new_row[j] = new_row[j-1] (from left) + row[j] (from above)
            new_row[j] = new_row[j-1] + row[j]
        row = new_row
        
    return row[n-1]


def main():
    m, n = 3, 7
    print(f"--- Unique Paths for a {m}x{n} grid ---")
    print(f"Tabulation solution: {unique_paths_tabulation(m, n)}")
    print(f"Optimized solution: {unique_paths_optimized(m, n)}")
    # Expected output: 28
    print("-" * 20)
    
    m, n = 3, 2
    print(f"--- Unique Paths for a {m}x{n} grid ---")
    print(f"Tabulation solution: {unique_paths_tabulation(m, n)}")
    print(f"Optimized solution: {unique_paths_optimized(m, n)}")
    # Expected output: 3
    print("-" * 20)

if __name__ == "__main__":
    main() 