from collections import deque

def is_valid_parentheses(s: str) -> bool:
    """
    Problem: Given a string containing '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid. An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

    Approach:
    Use a stack. Iterate through the string. If we see an opening bracket,
    push it onto the stack. If we see a closing bracket, check if the stack
    is empty or if the top of the stack is not the corresponding opening
    bracket. If so, the string is invalid. If we finish the loop and the
    stack is empty, the string is valid.

    Time Complexity: O(n) because we iterate through the string once.
    Space Complexity: O(n) in the worst case (e.g., "((((("))).
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:  # It's a closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:  # It's an opening bracket
            stack.append(char)
            
    return not stack

class MinStack:
    """
    Problem: Design a stack that supports push, pop, top, and getMin in O(1) time.

    Approach:
    Use two stacks. The main stack works as usual. The second stack, `min_stack`,
    keeps track of the minimum value at each stage. When we push a new value,
    we push the smaller of that value and the current min onto `min_stack`.
    When we pop, we pop from both stacks.

    Time Complexity: O(1) for all operations.
    Space Complexity: O(n) for the two stacks.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
        
def eval_rpn(tokens: list[str]) -> int:
    """
    Problem: Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Approach:
    Use a stack. Iterate through the tokens. If a token is a number, push it onto
    the stack. If it's an operator, pop the top two numbers, perform the operation,
    and push the result back onto the stack. The final result is the last item
    remaining in the stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    operators = {"+", "-", "*", "/"}
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else: # division, handle truncation towards zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))
            
    return stack[0]

def daily_temperatures(temps: list[int]) -> list[int]:
    """
    Problem: Given a list of daily temperatures, return a list where each element
    is the number of days you have to wait until a warmer temperature. If there
    is no future day for which this is possible, keep 0 instead.

    Approach (Monotonic Stack):
    Use a stack to store indices of the temperatures. We iterate through the temps.
    For each temperature, we check if it's warmer than the temp at the index on top
    of the stack. If it is, we've found the answer for that day. We pop the stack,
    calculate the day difference, and update our result array. We repeat this until
    the stack is empty or the current temp is not warmer. Then, push the current index.

    Time Complexity: O(n) because each index is pushed and popped at most once.
    Space Complexity: O(n) in the worst case (e.g., a decreasing list of temps).
    """
    n = len(temps)
    result = [0] * n
    stack = [] # stack of indices

    for i, temp in enumerate(temps):
        while stack and temp > temps[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
        
    return result

def main():
    print("--- Valid Parentheses ---")
    s1 = "()[]{}"
    s2 = "([)]"
    s3 = "{[]}"
    print(f"'{s1}' is valid: {is_valid_parentheses(s1)}")
    print(f"'{s2}' is valid: {is_valid_parentheses(s2)}")
    print(f"'{s3}' is valid: {is_valid_parentheses(s3)}")
    print("-" * 20)
    
    print("--- Min Stack ---")
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"Min element is: {min_stack.getMin()}") # returns -3
    min_stack.pop()
    print("Popped an element.")
    print(f"Top element is: {min_stack.top()}") # returns 0
    print(f"Min element is: {min_stack.getMin()}") # returns -2
    print("-" * 20)

    print("--- Evaluate RPN ---")
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(f"Expression: {tokens}")
    print(f"Result: {eval_rpn(tokens)}") # Should be 22
    print("-" * 20)

    print("--- Daily Temperatures ---")
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Temperatures: {temps}")
    print(f"Days to wait: {daily_temperatures(temps)}")
    print("-" * 20)


if __name__ == "__main__":
    main() 