from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Problem: Given an array of strings, group the anagrams together.

    Approach:
    Use a hash table (dictionary) to group the strings. The key insight is
    that all anagrams of a word become identical when their characters are
    sorted. This sorted version can serve as a "signature" or key in our
    hash table.

    1. Initialize a dictionary, `anagram_groups`, where the values will be lists.
       `defaultdict(list)` is ideal for this.
    2. Iterate through each string in the input list.
    3. For each string, create its canonical key by sorting its characters.
       We use a tuple of the sorted characters because lists cannot be
       dictionary keys, but tuples can.
    4. Append the original string to the list associated with its key in the
       dictionary.
    5. The values of the dictionary are the final grouped anagrams.

    Time Complexity: O(n * k log k), where n is the number of strings and
    k is the maximum length of a string. Sorting each string dominates the
    runtime.
    Space Complexity: O(n * k) to store the hash map and the grouped strings.
    """
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # sorted() returns a list of chars. We make it a tuple to be a dict key.
        key = tuple(sorted(s))
        anagram_groups[key].append(s)
        
    return list(anagram_groups.values())

def main():
    print("--- Group Anagrams ---")
    
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: {input_strs}")
    
    output = group_anagrams(input_strs)
    # The output order of groups doesn't matter.
    print(f"Output: {output}")
    print("-" * 20)

    input_strs_2 = ["", "b"]
    print(f"Input: {input_strs_2}")
    output_2 = group_anagrams(input_strs_2)
    print(f"Output: {output_2}")
    print("-" * 20)
    
    input_strs_3 = ["a"]
    print(f"Input: {input_strs_3}")
    output_3 = group_anagrams(input_strs_3)
    print(f"Output: {output_3}")
    print("-" * 20)

if __name__ == "__main__":
    main() 