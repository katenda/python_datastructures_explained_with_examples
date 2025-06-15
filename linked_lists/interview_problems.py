# linked_lists/interview_problems.py

"""
This file contains solutions to common linked list interview questions.
Each function is self-contained and operates on a head node.
"""

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

# Helper functions for testing
def create_linked_list(values):
    """Creates a linked list from a list of values."""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    """Prints the linked list."""
    if not head:
        print("None")
        return
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" -> ".join(elements))

# --- Interview Problems ---

def reverse_linked_list(head):
    """
    Problem: Reverse a singly linked list.

    Approach (Iterative):
    We use three pointers: prev, current, and next_node.
    - `prev` starts as None.
    - `current` starts at the head.
    - We iterate through the list, and for each node, we store its `next` node,
      then we reverse the `current` node's pointer to point to `prev`.
      Finally, we move `prev` and `current` one step forward.

    Time Complexity: O(n) because we visit each node once.
    Space Complexity: O(1) as we only use a few pointers.
    """
    prev = None
    current = head
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current node
        current = next_node       # Move to the next node
    return prev  # `prev` is the new head

def reverse_linked_list_recursive(head):
    """
    Problem: Reverse a singly linked list using recursion.

    Approach (Recursive):
    The base case is an empty list or a list with a single node, in which case
    the list is already reversed.
    For the recursive step, we call the function on the rest of the list (head.next).
    This call will reverse the sub-list and return its new head.
    We then need to attach the current `head` to the end of this reversed sub-list.
    We do this by making `head.next.next` point back to `head`.
    Finally, we set `head.next` to None to break the original forward link.

    Time Complexity: O(n) because we visit each node once.
    Space Complexity: O(n) due to the recursion call stack depth.
    """
    # Base case: if head is None or it's the last node
    if not head or not head.next:
        return head

    # Recursively reverse the sub-list and get the new head
    new_head = reverse_linked_list_recursive(head.next)

    # Reverse the link for the current node
    head.next.next = head
    head.next = None

    return new_head

def find_middle(head):
    """
    Problem: Find the middle node of a linked list. If the list has an even number
    of nodes, return the second of the two middle nodes.

    Approach (Fast and Slow Pointers):
    We use two pointers, `slow` and `fast`.
    - `slow` moves one step at a time.
    - `fast` moves two steps at a time.
    When `fast` reaches the end of the list, `slow` will be at the middle.

    Time Complexity: O(n) because we traverse half the list.
    Space Complexity: O(1).
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_two_sorted_lists(l1, l2):
    """
    Problem: Merge two sorted linked lists and return it as a new sorted list.

    Approach:
    Create a dummy node to serve as the starting point of the merged list.
    Use a `current` pointer to build the new list.
    Compare the nodes from `l1` and `l2`, and append the smaller one to the
    `current` pointer. Advance the pointer of the list from which the node was taken.
    Once one list is exhausted, append the remainder of the other list.

    Time Complexity: O(m + n), where m and n are the lengths of the two lists.
    Space Complexity: O(1) if we reuse nodes, or O(m + n) if new nodes are created. Here we reuse.
    """
    dummy = Node(0)
    current = dummy
    
    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
        
    # Append the remaining part
    if l1:
        current.next = l1
    elif l2:
        current.next = l2
        
    return dummy.next

def has_cycle(head):
    """
    Problem: Determine if a linked list has a cycle in it.

    Approach (Fast and Slow Pointers):
    This is also known as Floyd's Tortoise and Hare algorithm.
    Use two pointers, `slow` and `fast`. `slow` moves one step, and `fast` moves two.
    If there is a cycle, the `fast` pointer will eventually lap the `slow` pointer,
    and they will meet. If `fast` reaches the end of the list (None), there is no cycle.

    Time Complexity: O(n).
    Space Complexity: O(1).
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def remove_nth_from_end(head, n):
    """
    Problem: Remove the n-th node from the end of the list and return its head.

    Approach (Two Pointers):
    Use two pointers, `fast` and `slow`.
    First, move the `fast` pointer `n` steps ahead.
    Then, move both `fast` and `slow` together until `fast` reaches the end.
    At this point, `slow` will be at the node just before the one to be deleted.
    A dummy node is used to handle the edge case of deleting the head.

    Time Complexity: O(n) as it's a single pass.
    Space Complexity: O(1).
    """
    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    # Delete the node
    slow.next = slow.next.next
    return dummy.next

def main():
    print("--- Reverse Linked List ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original:"); print_linked_list(head)
    reversed_head = reverse_linked_list(head)
    print("Reversed:"); print_linked_list(reversed_head)
    print("-" * 20)
    
    print("--- Reverse Linked List (Recursive) ---")
    head_rec = create_linked_list([1, 2, 3, 4, 5])
    print("Original:"); print_linked_list(head_rec)
    reversed_head_rec = reverse_linked_list_recursive(head_rec)
    print("Reversed:"); print_linked_list(reversed_head_rec)
    print("-" * 20)

    print("--- Find Middle Node ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    middle = find_middle(head)
    print("List:"); print_linked_list(head)
    print(f"Middle node data: {middle.data}")
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    middle = find_middle(head)
    print("List:"); print_linked_list(head)
    print(f"Middle node data: {middle.data}")
    print("-" * 20)

    print("--- Merge Two Sorted Lists ---")
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    print("List 1:"); print_linked_list(l1)
    print("List 2:"); print_linked_list(l2)
    merged_head = merge_two_sorted_lists(l1, l2)
    print("Merged:"); print_linked_list(merged_head)
    print("-" * 20)

    print("--- Detect Cycle ---")
    head_no_cycle = create_linked_list([1, 2, 3, 4])
    print("List with no cycle:"); print_linked_list(head_no_cycle)
    print(f"Has cycle: {has_cycle(head_no_cycle)}")
    
    head_with_cycle = create_linked_list([1, 2, 3, 4])
    head_with_cycle.next.next.next.next = head_with_cycle.next # 4 -> 2
    print("List with cycle (4 -> 2):")
    print(f"Has cycle: {has_cycle(head_with_cycle)}")
    print("-" * 20)

    print("--- Remove Nth Node From End ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original:"); print_linked_list(head)
    head = remove_nth_from_end(head, 2)
    print("After removing 2nd from end:"); print_linked_list(head)
    
    head2 = create_linked_list([1])
    print("Original:"); print_linked_list(head2)
    head2 = remove_nth_from_end(head2, 1)
    print("After removing 1st from end:"); print_linked_list(head2)
    print("-" * 20)


if __name__ == "__main__":
    main() 