# core_python_types/tuple_examples.py

def demonstrate_tuple_properties():
    """
    Demonstrates the core properties of tuples: ordered and immutable.
    """
    print("--- Tuple Properties ---")
    
    # 1. Creating a tuple
    my_tuple = ("apple", "banana", "cherry")
    print(f"My tuple: {my_tuple}")
    
    # 2. They are ordered and can be indexed
    print(f"First element: {my_tuple[0]}")
    print(f"Last element: {my_tuple[-1]}")
    
    # 3. They are IMMUTABLE. The following lines will cause a TypeError if uncommented.
    print("\nAttempting to change a tuple will raise a TypeError.")
    try:
        my_tuple[0] = "apricot"
    except TypeError as e:
        print(f"Caught expected error: {e}")
        
    # Tuples do not have methods like .append() or .remove()
    print("Tuples do not have methods like .append() or .remove().")

    print("-" * 20)


def demonstrate_tuple_hashability():
    """
    Demonstrates the key advantage of tuples: they are hashable and can be
    used as dictionary keys.
    """
    print("--- Tuple Hashability (Their Superpower) ---")
    
    # Use tuples as dictionary keys to store coordinates
    locations = {
        (35.6895, 139.6917): "Tokyo",
        (40.7128, -74.0060): "New York",
        (48.8566, 2.3522): "Paris"
    }
    
    print("Using tuples as dictionary keys for coordinates:")
    print(locations)
    
    # This would fail with a list
    print("\nAttempting to use a list as a key will raise a TypeError.")
    try:
        locations[[51.5074, -0.1278]] = "London"
    except TypeError as e:
        print(f"Caught expected error: {e}")
        
    print("-" * 20)

def main():
    demonstrate_tuple_properties()
    demonstrate_tuple_hashability()

if __name__ == "__main__":
    main() 