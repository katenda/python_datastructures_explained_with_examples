
######################
### STACK IMPLEMENTATION
########################
# Creating a stack
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed item: {item}")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack


######################
#### END OF STACK IMPLEMENTATION


#define main function
def main():
    print("Welcome to python data structures")
    #CREATE A STACK HERE
    s = Stack()
    s.push("1")
    s.push("2")
    s.push("3")

    print("Top of stack:", s.peek())
    print("Popped item:", s.pop())
    print("Stack after pop:", s.display())
    print("Is empty:", s.is_empty())

    print("****************************************************\n")
    print("NOTE: For the array-based implementation of a stack, the push and pop operations take constant time\n")
    print("****************************************************\n")


#call main function
if __name__=="__main__":
    main()

