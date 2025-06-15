# advanced_problems/trie.py

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self):
        # Each node has a dictionary to store its children, mapping char -> TrieNode
        self.children = {}
        # is_end_of_word is True if the node represents the end of a word
        self.is_end_of_word = False

class Trie:
    """
    An implementation of a Trie (Prefix Tree).
    """
    def __init__(self):
        """Initializes the data structure."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.

        Time Complexity: O(L), where L is the length of the word.
        Space Complexity: O(L) in the worst case (for a new word).
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.

        Time Complexity: O(L), where L is the length of the word.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.

        Time Complexity: O(L), where L is the length of the prefix.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

def main():
    print("--- Trie (Prefix Tree) Demonstration ---")
    trie = Trie()

    print("Inserting 'apple'...")
    trie.insert("apple")

    print(f"Search for 'apple': {trie.search('apple')}")     # returns True
    print(f"Search for 'app': {trie.search('app')}")       # returns False
    print(f"Starts with 'app': {trie.startsWith('app')}")   # returns True

    print("\nInserting 'app'...")
    trie.insert("app")
    print(f"Search for 'app': {trie.search('app')}")       # returns True
    
    print("\nInserting 'application'...")
    trie.insert("application")
    print(f"Starts with 'appl': {trie.startsWith('appl')}") # returns True

    print("-" * 20)

if __name__ == "__main__":
    main() 