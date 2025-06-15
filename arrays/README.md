# Arrays

An array is a fundamental data structure that stores a collection of elements of the same type in contiguous memory locations. This allows for efficient access to elements using their index.

In Python, the `list` type serves as a dynamic array, which can grow and shrink as needed.

## Time Complexity of Array Operations

| Operation      | Big O      | Notes                                                |
|----------------|------------|------------------------------------------------------|
| Access         | O(1)       | Fast access to elements by index.                    |
| Search         | O(n)       | Linear search through the array.                     |
| Insertion      | O(n)       | Requires shifting elements. Appending is O(1) amortized. |
| Deletion       | O(n)       | Requires shifting elements.                          |
|                |            |                                                      |
## Python `list` as a Dynamic Array

Python's `list` provides a convenient and powerful implementation of a dynamic array. Here are some common operations:

*   **Creating a list**: `my_list = [1, 2, 3, 4, 5]`
*   **Accessing elements**: `my_list[0]`  # Returns 1
*   **Appending elements**: `my_list.append(6)`
*   **Inserting elements**: `my_list.insert(1, 10)`  # Inserts 10 at index 1
*   **Removing elements**: `my_list.remove(3)`
*   **Slicing**: `my_list[1:3]`  # Returns a new list `[10, 2]`

We will now look at some code examples. 