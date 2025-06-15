# array_examples.py

def main():
    # 1. Create a list (dynamic array)
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"Initial list of fruits: {fruits}")

    # 2. Accessing elements (O(1))
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")

    # 3. Appending an element (Amortized O(1))
    fruits.append("elderberry")
    print(f"List after appending 'elderberry': {fruits}")

    # 4. Inserting an element (O(n))
    fruits.insert(2, "coconut")
    print(f"List after inserting 'coconut' at index 2: {fruits}")

    # 5. Removing an element (O(n))
    fruits.remove("banana")
    print(f"List after removing 'banana': {fruits}")

    # 6. Searching for an element (O(n))
    if "cherry" in fruits:
        cherry_index = fruits.index("cherry")
        print(f"'cherry' found at index: {cherry_index}")
    else:
        print("'cherry' not found in the list.")

    # 7. Slicing the list
    # Slicing creates a new list
    first_two_fruits = fruits[0:2]
    print(f"First two fruits (slice): {first_two_fruits}")

    # 8. Iterating through a list
    print("Iterating through the list:")
    for fruit in fruits:
        print(f"- {fruit}")

if __name__ == "__main__":
    main() 