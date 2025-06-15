# linked_lists/lru_cache.py

class Node:
    """
    A node for the doubly linked list. It stores a key-value pair,
    which is essential for the cache.
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    An implementation of a Least Recently Used (LRU) Cache.
    It combines a hash map for O(1) lookups and a doubly linked list
    for O(1) additions and removals of nodes to maintain usage order.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map: key -> Node

        # Dummy head and tail nodes to handle edge cases gracefully.
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Removes a node from the linked list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_front(self, node: Node):
        """Adds a node right after the dummy head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """
        Retrieves an item from the cache. If found, it moves the item
        to the front of the list to mark it as most recently used.
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Adds or updates an item in the cache. If the key exists, it updates
        the value and moves it to the front. If not, it adds a new item.
        If the cache is full, it evicts the least recently used item.
        """
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            self._remove(node)
            node.val = value
            self._add_to_front(node)
        else:
            # Add new node
            if len(self.cache) == self.capacity:
                # Evict the least recently used item (the one before the tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


def main():
    print("--- LRU Cache Demonstration ---")
    
    # Initialize cache with capacity 2
    lru_cache = LRUCache(2)

    lru_cache.put(1, 1)    # Cache is {1: 1}
    print("put(1, 1)")
    
    lru_cache.put(2, 2)    # Cache is {1: 1, 2: 2}
    print("put(2, 2)")
    
    val = lru_cache.get(1) # Returns 1, Cache is {2: 2, 1: 1} (1 is now most recent)
    print(f"get(1): returns {val}")

    lru_cache.put(3, 3)    # LRU key 2 was evicted. Cache is {1: 1, 3: 3}
    print("put(3, 3) -> evicts key 2")

    val = lru_cache.get(2) # Returns -1 (not found)
    print(f"get(2): returns {val}")

    lru_cache.put(4, 4)    # LRU key 1 was evicted. Cache is {3: 3, 4: 4}
    print("put(4, 4) -> evicts key 1")

    val = lru_cache.get(1) # Returns -1 (not found)
    print(f"get(1): returns {val}")

    val = lru_cache.get(3) # Returns 3, Cache is {4: 4, 3: 3}
    print(f"get(3): returns {val}")

    val = lru_cache.get(4) # Returns 4, Cache is {3: 3, 4: 4}
    print(f"get(4): returns {val}")
    print("-" * 20)

if __name__ == "__main__":
    main() 