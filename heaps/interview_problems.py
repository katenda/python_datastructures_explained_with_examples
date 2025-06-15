# heaps/interview_problems.py
import heapq
from collections import Counter

# --- Problem 1: Kth Largest Element in an Array ---

def find_kth_largest(nums: list[int], k: int) -> int:
    """
    Problem: Find the k-th largest element in an unsorted array.

    Approach:
    Use a min-heap of size k. Iterate through the numbers.
    - Push each number onto the heap.
    - If the heap's size grows larger than k, pop the smallest element.
    By the end, the heap contains the k largest elements from the array,
    and the root of the min-heap is the k-th largest element.

    Time Complexity: O(n log k). We iterate through n elements, and each
    heap operation takes O(log k) time.
    Space Complexity: O(k) to store the heap.
    """
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

# --- Problem 2: Top K Frequent Elements ---

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Problem: Given an integer array nums and an integer k, return the k
    most frequent elements.

    Approach:
    1. Count the frequency of each number using a hash map (Counter).
    2. Use a min-heap to find the top k frequent elements. The heap will
       store tuples of (frequency, number).
    3. Iterate through the frequency map. For each (number, freq) pair,
       push (freq, number) to the heap. If the heap size exceeds k, pop.
    4. The final heap contains the top k elements. Extract the numbers.

    Time Complexity: O(n log k). O(n) to build the frequency map, then
    O(n log k) for the heap operations.
    Space Complexity: O(n) for the frequency map and O(k) for the heap.
    """
    if k == len(nums):
        return nums

    counts = Counter(nums)
    min_heap = []
    for num, freq in counts.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return [num for freq, num in min_heap]

# --- Problem 3: Find Median from Data Stream ---

class MedianFinder:
    """
    Problem: Design a data structure that supports adding numbers from a
    stream and finding the median.

    Approach:
    Use two heaps:
    - A max-heap (`small`) to store the smaller half of the numbers.
    - A min-heap (`large`) to store the larger half of the numbers.

    The heaps are kept balanced such that `len(small)` is either equal to
    or one greater than `len(large)`.
    - `addNum`: Add to `small` first. Then, move the largest from `small` to
      `large`. If `large` becomes bigger, move its smallest to `small`.
    - `findMedian`: If sizes are unequal, the median is the root of `small`.
      If equal, it's the average of the roots of both heaps.

    Time Complexity: `addNum` is O(log n), `findMedian` is O(1).
    Space Complexity: O(n) to store all numbers.
    """
    def __init__(self):
        # `small` is a max-heap, storing the smaller half of numbers (negated)
        self.small = []
        # `large` is a min-heap, storing the larger half of numbers
        self.large = []

    def addNum(self, num: int) -> None:
        # Push to max-heap (negated) and pop the largest (smallest negative)
        heapq.heappush(self.small, -num)
        largest_in_small = -heapq.heappop(self.small)
        
        # Push that element to the min-heap
        heapq.heappush(self.large, largest_in_small)
        
        # Balance the heaps if necessary
        if len(self.large) > len(self.small):
            smallest_in_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_in_large)

    def findMedian(self) -> float:
        # If small heap has more elements, the median is its root
        if len(self.small) > len(self.large):
            return -self.small[0]
        # Otherwise, it's the average of the two roots
        return (-self.small[0] + self.large[0]) / 2.0


def main():
    print("--- Kth Largest Element ---")
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"In {nums}, the {k}nd largest element is: {find_kth_largest(nums, k)}")
    print("-" * 20)
    
    print("--- Top K Frequent Elements ---")
    nums = [1,1,1,2,2,3]
    k = 2
    print(f"In {nums}, top {k} frequent elements are: {top_k_frequent(nums, k)}")
    print("-" * 20)

    print("--- Median from Data Stream ---")
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(f"Median after adding 1, 2 is: {medianFinder.findMedian()}") # 1.5
    medianFinder.addNum(3)
    print(f"Median after adding 3 is: {medianFinder.findMedian()}")   # 2
    print("-" * 20)


if __name__ == "__main__":
    main() 