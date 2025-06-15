from collections import deque

def demonstrate_list_as_stack():
    """Demonstrates using a Python list as a stack."""
    print("--- Using list as a Stack ---")
    
    stack = []
    
    # Push operations
    stack.append("A")
    stack.append("B")
    stack.append("C")
    print(f"Stack after pushes: {stack}")
    
    # Peek operation
    if stack:
        print(f"Top element (peek): {stack[-1]}")
    
    # Pop operations
    item = stack.pop()
    print(f"Popped item: {item}")
    print(f"Stack after one pop: {stack}")
    
    item = stack.pop()
    print(f"Popped item: {item}")
    
    item = stack.pop()
    print(f"Popped item: {item}")
    
    # Check if empty
    if not stack:
        print("Stack is now empty.")
    
    # Trying to pop from an empty stack will raise an IndexError
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error when popping from empty stack: {e}")
    print("-" * 20)


def demonstrate_deque_as_stack():
    """Demonstrates using collections.deque as a stack (recommended)."""
    print("--- Using collections.deque as a Stack ---")
    
    stack = deque()
    
    # Push operations
    stack.append("A")
    stack.append("B")
    stack.append("C")
    print(f"Stack after pushes: {stack}")
    
    # Peek operation
    if stack:
        print(f"Top element (peek): {stack[-1]}")
        
    # Pop operations
    item = stack.pop()
    print(f"Popped item: {item}")
    print(f"Stack after one pop: {stack}")
    
    item = stack.pop()
    print(f"Popped item: {item}")
    
    item = stack.pop()
    print(f"Popped item: {item}")
    
    # Check if empty
    if not stack:
        print("Stack is now empty.")
        
    # Trying to pop from an empty deque will also raise an IndexError
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error when popping from empty deque: {e}")
    print("-" * 20)

def main():
    demonstrate_list_as_stack()
    demonstrate_deque_as_stack()

if __name__ == "__main__":
    main() 