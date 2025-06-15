from collections import deque

def demonstrate_deque_as_queue():
    """
    Demonstrates using collections.deque as a queue (the recommended method).
    - enqueue: append()
    - dequeue: popleft()
    - peek: queue[0]
    """
    print("--- Using collections.deque as a Queue (Recommended) ---")
    
    queue = deque()
    
    # Enqueue operations
    print("Enqueuing A, B, C...")
    queue.append("A")  # Enqueue
    queue.append("B")
    queue.append("C")
    print(f"Queue state: {queue}")
    
    # Peek operation
    if queue:
        print(f"Front element (peek): {queue[0]}")
    
    # Dequeue operations
    item = queue.popleft() # Dequeue
    print(f"Dequeued item: {item}")
    print(f"Queue after one dequeue: {queue}")
    
    item = queue.popleft()
    print(f"Dequeued item: {item}")
    
    item = queue.popleft()
    print(f"Dequeued item: {item}")
    
    # Check if empty
    if not queue:
        print("Queue is now empty.")
        
    # Trying to pop from an empty deque will raise an IndexError
    try:
        queue.popleft()
    except IndexError as e:
        print(f"Error when dequeuing from empty queue: {e}")
    print("-" * 20)


def demonstrate_list_as_queue():
    """
    Demonstrates using a list as a queue (inefficient and not recommended).
    - enqueue: append()
    - dequeue: pop(0) -> This is the O(n) operation.
    """
    print("--- Using list as a Queue (Inefficient) ---")
    
    queue = []
    
    print("Enqueuing A, B, C...")
    queue.append("A")
    queue.append("B")
    queue.append("C")
    print(f"Queue state: {queue}")

    # Dequeue operation (the slow part)
    item = queue.pop(0)
    print(f"Dequeued item: {item}")
    print(f"Queue after one dequeue: {queue}")
    
    item = queue.pop(0)
    print(f"Dequeued item: {item}")
    print(f"Queue state: {queue}")
    print("-" * 20)

def main():
    demonstrate_deque_as_queue()
    demonstrate_list_as_queue()

if __name__ == "__main__":
    main() 