# Big O Notation

Big O notation is used in computer science to describe the performance or complexity of an algorithm. It tells you how the runtime of an algorithm grows as the input size grows. Understanding Big O is crucial for writing efficient code and for choosing the right data structure for a particular problem.

Here are some of the most common complexities:

*   **O(1) - Constant Time**: The execution time is always the same, regardless of the size of the input.
    *   *Example*: Accessing an element in an array by its index.
*   **O(log n) - Logarithmic Time**: The execution time grows logarithmically with the input size. This is very efficient for large inputs.
    *   *Example*: Finding an element in a balanced binary search tree.
*   **O(n) - Linear Time**: The execution time is directly proportional to the input size.
    *   *Example*: Iterating through all elements in a list.
*   **O(n log n) - Log-Linear Time**: A very common complexity for efficient sorting algorithms.
    *   *Example*: Merge sort or quicksort.
*   **O(n²) - Quadratic Time**: The execution time is proportional to the square of the input size. This becomes slow very quickly.
    *   *Example*: Nested loops iterating over the same list.
*   **O(2ⁿ) - Exponential Time**: The execution time doubles for each new element in the input. This is generally too slow for anything but very small input sizes.
    *   *Example*: The recursive calculation of Fibonacci numbers without memoization. 