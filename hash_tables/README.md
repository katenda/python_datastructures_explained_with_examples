# Hash Tables

A hash table is a data structure used to store key-value pairs. It uses a **hash function** to compute an index into an array of buckets or slots, from which the desired value can be found. This allows for extremely fast average-case lookups, insertions, and deletions.

In Python, the built-in `dict` (dictionary) and `set` types are implemented using hash tables.

## How It Works

1.  **Hashing**: When a key-value pair is added, the key is passed to a hash function, which generates a numerical hash code.
2.  **Indexing**: This hash code is then mapped to an index in an underlying array. A common way to do this is `index = hash_code % array_size`.
3.  **Storage**: The value is stored at that computed index.

This direct computation allows for an average time complexity of O(1) for accessing an element.

## Collision Resolution

A **collision** occurs when two different keys hash to the same index. A common method to resolve this is **Separate Chaining**.

*   **Separate Chaining**: Instead of storing a single value, each bucket in the array stores a pointer to a data structure like a linked list. If a collision occurs, the new key-value pair is simply appended to the linked list at that index. During a lookup, the hash table finds the correct bucket and then iterates through the linked list to find the key.

## Performance

| Operation | Average Case | Worst Case                                                                    |
|-----------|--------------|-------------------------------------------------------------------------------|
| Search    | O(1)         | O(n)                                                                          |
| Insert    | O(1)         | O(n)                                                                          |
| Delete    | O(1)         | O(n)                                                                          |

The **worst case** of O(n) occurs if the hash function is poor and causes most keys to collide into a single bucket, effectively degrading performance to that of a linked list. However, with well-designed hash functions, hash tables are one of the most efficient data structures for lookups. 