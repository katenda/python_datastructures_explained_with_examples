# dynamic_programming/house_robber.py

# --- 1. Bottom-Up Dynamic Programming with Tabulation ---

def rob_tabulation(nums: list[int]) -> int:
    """
    Solves the House Robber problem using a DP table.
    dp[i] = the maximum amount of money that can be robbed up to house i.

    Recurrence Relation:
    dp[i] = max(rob_house_i, dont_rob_house_i)
    dp[i] = max(nums[i] + dp[i-2], dp[i-1])

    Time Complexity: O(n)
    Space Complexity: O(n) for the dp table.
    """
    if not nums:
        return 0
    n = len(nums)
    if n <= 2:
        return max(nums)
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
    return dp[n-1]

# --- 2. Bottom-Up DP with Space Optimization ---

def rob_optimized(nums: list[int]) -> int:
    """
    This version optimizes the space complexity. To calculate the result
    for the current house `i`, we only need to know the results for the
    previous two houses (`i-1` and `i-2`). We can store these in two
    variables instead of a full DP array.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    # We use two variables to represent dp[i-1] and dp[i-2]
    rob_prev_house = 0  # Represents dp[i-1]
    rob_two_houses_ago = 0 # Represents dp[i-2]
    
    # [rob_two_houses_ago, rob_prev_house, num, num+1, ...]
    for num in nums:
        # The new rob_prev_house will be the max of robbing the current house
        # or not robbing it.
        temp = max(num + rob_two_houses_ago, rob_prev_house)
        rob_two_houses_ago = rob_prev_house
        rob_prev_house = temp
        
    return rob_prev_house


def main():
    nums1 = [1, 2, 3, 1]
    print(f"--- House Robber for nums = {nums1} ---")
    print(f"Tabulation solution: {rob_tabulation(list(nums1))}")
    print(f"Optimized solution: {rob_optimized(list(nums1))}")
    # Expected output: 4 (Rob house 1 and 3)
    print("-" * 20)
    
    nums2 = [2, 7, 9, 3, 1]
    print(f"--- House Robber for nums = {nums2} ---")
    print(f"Tabulation solution: {rob_tabulation(list(nums2))}")
    print(f"Optimized solution: {rob_optimized(list(nums2))}")
    # Expected output: 12 (Rob house 2, 9, 1)
    print("-" * 20)

if __name__ == "__main__":
    main() 