# hash_tables/hash_table_examples.py

def demonstrate_dictionary():
    """
    Demonstrates the usage of Python's dict (a hash table).
    """
    print("--- Dictionary (dict) Demonstration ---")
    
    # 1. Create a dictionary
    student_ages = {"Alice": 21, "Bob": 22, "Charlie": 20}
    print(f"Initial dictionary: {student_ages}")
    
    # 2. Add or update items (O(1) on average)
    student_ages["David"] = 23  # Add a new entry
    student_ages["Alice"] = 22  # Update an existing entry
    print(f"After adding David and updating Alice: {student_ages}")
    
    # 3. Access an item (O(1) on average)
    print(f"Bob's age is: {student_ages['Bob']}")
    
    # 4. Check for key existence (O(1) on average)
    print(f"Is 'Charlie' in the dictionary? {'Charlie' in student_ages}")
    print(f"Is 'Eve' in the dictionary? {'Eve' in student_ages}")
    
    # 5. Delete an item (O(1) on average)
    del student_ages["Charlie"]
    print(f"After deleting Charlie: {student_ages}")
    
    # 6. Iterate through keys, values, or items
    print("\nIterating through the dictionary:")
    for name, age in student_ages.items():
        print(f"- {name} is {age} years old.")
        
    print("-" * 20)

def demonstrate_set():
    """
    Demonstrates the usage of Python's set (a hash table for unique items).
    """
    print("--- Set Demonstration ---")
    
    # 1. Create a set
    unique_items = {"apple", "banana", "cherry"}
    print(f"Initial set: {unique_items}")
    
    # 2. Add items (O(1) on average). Duplicates are ignored.
    unique_items.add("apple")
    unique_items.add("date")
    print(f"After adding 'apple' (duplicate) and 'date': {unique_items}")
    
    # 3. Check for membership (O(1) on average)
    print(f"Is 'banana' in the set? {'banana' in unique_items}")
    print(f"Is 'fig' in the set? {'fig' in unique_items}")
    
    # 4. Remove an item (O(1) on average)
    unique_items.remove("banana")
    print(f"After removing 'banana': {unique_items}")
    
    # Sets are also useful for mathematical set operations like union, intersection, etc.
    other_fruits = {"date", "elderberry"}
    print(f"Union with {other_fruits}: {unique_items.union(other_fruits)}")
    print(f"Intersection with {other_fruits}: {unique_items.intersection(other_fruits)}")
    
    print("-" * 20)
    
def main():
    demonstrate_dictionary()
    demonstrate_set()

if __name__ == "__main__":
    main() 