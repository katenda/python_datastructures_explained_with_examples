# arrays/interview_problems.py

"""
This file contains solutions to common array-based programming interview questions.
Each function includes an explanation of the approach, time complexity, and space complexity.
"""

def two_sum(nums, target):
    """
    Problem: Given an array of integers, return indices of the two numbers such
    that they add up to a specific target. You may assume that each input would
    have exactly one solution, and you may not use the same element twice.

    Approach: Use a hash map (dictionary in Python) to store the numbers we've seen
    and their indices. For each number, calculate its complement (target - number).
    If the complement is in the hash map, we have found our pair.

    Time Complexity: O(n) because we iterate through the list once.
    Space Complexity: O(n) because, in the worst case, we store all elements in the hash map.
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

def rotate_array(nums, k):
    """
    Problem: Rotate an array of n elements to the right by k steps.
    For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

    Approach: An efficient approach is to use slicing. We can split the array into two parts
    at the (n - k)-th index and then concatenate the second part before the first part.
    The modulo operator `%` is used to handle cases where k is greater than the length of the array.

    Time Complexity: O(n) because slicing and creating a new list takes time proportional to the number of elements.
    Space Complexity: O(n) as slicing creates new lists.
    """
    n = len(nums)
    k = k % n
    if k == 0:
        return nums
    
    # In-place modification of the original list
    nums[:] = nums[-k:] + nums[:-k]
    return nums

def contains_duplicate(nums):
    """
    Problem: Given an array of integers, find if the array contains any duplicates.
    Your function should return true if any value appears at least twice in the array,
    and it should return false if every element is distinct.

    Approach: Use a hash set to keep track of the elements we have seen.
    If we encounter a number that is already in the set, we have found a duplicate.

    Time Complexity: O(n) because we iterate through the list once.
    Space Complexity: O(n) because, in the worst case, we store all unique elements in the set.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def max_profit(prices):
    """
    Problem: Say you have an array for which the i-th element is the price of a given
    stock on day i. If you were only permitted to complete at most one transaction
    (i.e., buy one and sell one share of the stock), design an algorithm to find the
    maximum profit.

    Approach: Iterate through the prices while keeping track of the minimum price seen so far
    (the best day to buy). For each day, calculate the potential profit if we were to sell
    on that day. Update the maximum profit seen so far.

    Time Complexity: O(n) because we iterate through the list once.
    Space Complexity: O(1) as we only use a few variables to store state.
    """
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit

def move_zeroes(nums):
    """
    Problem: Given an array nums, write a function to move all 0's to the end of it
    while maintaining the relative order of the non-zero elements.
    This must be done in-place without making a copy of the array.

    Approach: Use a two-pointer technique. One pointer (`write_idx`) keeps track of
    the position where the next non-zero element should be written. The other pointer
    (the loop iterator `read_idx`) scans the array. When a non-zero element is found,
    it's placed at `write_idx`, and `write_idx` is incremented. After the first pass,
    all non-zero elements are at the beginning of the array in their original order.
    The rest of the array is then filled with zeros.

    Time Complexity: O(n) because we iterate through the list once.
    Space Complexity: O(1) because we modify the array in-place.
    """
    write_idx = 0
    for read_idx in range(len(nums)):
        if nums[read_idx] != 0:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
            
    for i in range(write_idx, len(nums)):
        nums[i] = 0
    
    return nums

def main():
    print("--- Two Sum ---")
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {two_sum(nums, target)}")
    print("-" * 20)

    print("--- Rotate Array ---")
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {rotate_array(list(nums), k)}") # Pass a copy
    print("-" * 20)

    print("--- Contains Duplicate ---")
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    print(f"Input: {nums1}")
    print(f"Output: {contains_duplicate(nums1)}")
    print(f"Input: {nums2}")
    print(f"Output: {contains_duplicate(nums2)}")
    print("-" * 20)

    print("--- Best Time to Buy and Sell Stock ---")
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Input: {prices}")
    print(f"Output: {max_profit(prices)}")
    print("-" * 20)
    
    print("--- Move Zeroes ---")
    nums = [0, 1, 0, 3, 12]
    print(f"Input: {nums}")
    print(f"Output: {move_zeroes(list(nums))}") # Pass a copy
    print("-" * 20)


if __name__ == "__main__":
    main() 