# dynamic_programming/climbing_stairs.py

# --- 1. Naive Recursive Solution (Exponential Time) ---

def climb_stairs_naive(n: int) -> int:
    """
    This solution is correct but very slow (O(2^n)) because it re-computes
    the same subproblems many times. It will time out on larger inputs.
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs_naive(n - 1) + climb_stairs_naive(n - 2)

# --- 2. Top-Down Dynamic Programming with Memoization ---

def climb_stairs_memo(n: int) -> int:
    """
    This is the top-down DP approach. We use a cache (memo) to store the
    results of subproblems we've already solved.

    Time Complexity: O(n), because each subproblem is solved only once.
    Space Complexity: O(n) for the cache and recursion stack.
    """
    memo = {}
    def solve(k):
        if k in memo:
            return memo[k]
        if k <= 2:
            return k
        
        memo[k] = solve(k - 1) + solve(k - 2)
        return memo[k]
    
    return solve(n)

# --- 3. Bottom-Up Dynamic Programming with Tabulation ---

def climb_stairs_tabulation(n: int) -> int:
    """
    This is the bottom-up DP approach. We build the solution iteratively
    from the smallest subproblems.

    Time Complexity: O(n)
    Space Complexity: O(n) for the dp table.
    """
    if n <= 2:
        return n
    
    # dp[i] will store the number of ways to reach step i
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

# --- 4. Bottom-Up with Space Optimization ---

def climb_stairs_optimized(n: int) -> int:
    """
    We can optimize the tabulation approach. Notice we only ever need the
    last two values (i-1 and i-2) to compute the current value. We don't
    need the whole table.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 2:
        return n
    
    one_step_back = 2
    two_steps_back = 1
    
    for _ in range(3, n + 1):
        current = one_step_back + two_steps_back
        two_steps_back = one_step_back
        one_step_back = current
        
    return one_step_back

def main():
    n = 10
    print(f"--- Climbing Stairs for n = {n} ---")
    
    # print(f"Naive recursive solution: {climb_stairs_naive(35)}") # Very slow!
    print(f"Top-Down DP with Memoization: {climb_stairs_memo(n)}")
    print(f"Bottom-Up DP with Tabulation: {climb_stairs_tabulation(n)}")
    print(f"Bottom-Up DP (Optimized Space): {climb_stairs_optimized(n)}")
    print("-" * 20)
    
    n = 45 # A number large enough to cause timeouts for the naive approach
    print(f"--- Climbing Stairs for n = {n} ---")
    print(f"Bottom-Up DP (Optimized Space): {climb_stairs_optimized(n)}")
    print("-" * 20)


if __name__ == "__main__":
    main() 