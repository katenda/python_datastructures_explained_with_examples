# heaps/heap_examples.py
import heapq

def demonstrate_min_heap():
    """
    Demonstrates the basic usage of the heapq module for a min-heap.
    """
    print("--- Min-Heap Demonstration (using heapq) ---")
    
    # heapq operates on a standard list
    min_heap = []
    
    # 1. Push items onto the heap
    heapq.heappush(min_heap, 4)
    heapq.heappush(min_heap, 1)
    heapq.heappush(min_heap, 7)
    heapq.heappush(min_heap, 3)
    
    # The list itself may not look sorted, but it satisfies the heap property.
    print(f"Internal list representation of the heap: {min_heap}")
    
    # 2. Peek at the smallest item (always at index 0)
    print(f"Smallest item (peek): {min_heap[0]}")
    
    # 3. Pop items from the heap (always the smallest)
    print("Popping items:")
    while min_heap:
        smallest = heapq.heappop(min_heap)
        print(f"Popped: {smallest}")
    
    print("-" * 20)

def build_heap_from_list():
    """
    Demonstrates building a heap from an existing list in O(n) time.
    """
    print("--- Building a Heap from a List ---")
    
    numbers = [9, 5, 2, 8, 1, 6]
    print(f"Original list: {numbers}")
    
    # Transform the list into a heap in-place
    heapq.heapify(numbers)
    
    print(f"List after heapify: {numbers}")
    print(f"Smallest element is {numbers[0]}")
    print("-" * 20)


def demonstrate_max_heap():
    """
    Demonstrates simulating a max-heap using heapq.
    The trick is to store the negative of the numbers.
    """
    print("--- Max-Heap Simulation ---")
    
    max_heap = []
    
    # Push negated values
    heapq.heappush(max_heap, -4)
    heapq.heappush(max_heap, -1)
    heapq.heappush(max_heap, -7)
    heapq.heappush(max_heap, -3)
    
    print(f"Internal max-heap representation: {max_heap}")
    
    # Peek at the largest item (negate the root)
    print(f"Largest item (peek): {-max_heap[0]}")
    
    # Pop the largest item
    largest = -heapq.heappop(max_heap)
    print(f"Popped largest item: {largest}")
    print(f"New largest item: {-max_heap[0]}")
    print("-" * 20)


def main():
    demonstrate_min_heap()
    build_heap_from_list()
    demonstrate_max_heap()

if __name__ == "__main__":
    main() 