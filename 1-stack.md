# Stack Data Structure

-[Home Page](https://github.com/KurtHermansen/Data-Structures/blob/master/0-welcome.md)

## Introduction
In computer programming, data structures are essential for organizing and manipulating data efficiently. One such data structure is a stack, which follows the Last-In-First-Out (LIFO) principle. A stack is a collection of elements in which items are added and removed from the same end, known as the top of the stack.

Imagine a stack of plates, where you can only add a new plate on top or remove the topmost plate. This real-world analogy perfectly illustrates how a stack operates. The last plate you placed on the stack will be the first one to be removed. This characteristic makes stacks ideal for managing data in certain scenarios.

The stack has two main operations: **push**, which adds an element to the top of the stack, and **pop**, which removes the topmost element from the stack. 

![Stack Picture](https://github.com/KurtHermansen/Data-Structures/blob/master/stack.jpg)

## Stack Operations
Stacks typically support the following operations:

### Push
The push operation adds an element to the top of the stack. It involves placing the new item on top of the existing elements. As a result, the new element becomes the new top of the stack.

### Pop
The pop operation removes and returns the element from the top of the stack. It effectively reverses the push operation by retrieving the topmost element and adjusting the stack accordingly.

### Peek
The peek operation allows you to access the element at the top of the stack without removing it. It is useful for examining the top element or performing certain operations based on its value.

### isEmpty
The isEmpty operation checks whether the stack is empty or not. It returns True if the stack contains no elements and False otherwise. This operation helps in handling edge cases and preventing errors when manipulating the stack.

### Size
The size operation returns the number of elements currently stored in the stack. It provides a convenient way to determine the stack's current capacity and track changes in its size over time.


## Pros and Cons
### Pros
- Simplicity: The stack has a simple and intuitive interface with only a few operations, making it easy to understand and implement.
- Efficient Operations: Both push and pop operations have a time complexity of O(1), which means they execute in constant time.
- Function Call Management: Stacks are useful for managing function calls, as they keep track of the execution order and return addresses.

### Cons
- Limited Access: Unlike other data structures like arrays, stacks provide access only to the topmost element. Accessing elements in the middle requires popping off the elements above them.
- Size Limit: Stacks have a fixed size, either determined by the underlying programming language or the implementation. If the stack exceeds its capacity, it results in a stack overflow error.

## Use Cases
- Function Call Tracking: Stacks are commonly used to manage function calls. When a function is called, its return address and local variables are pushed onto the stack. This allows the program to keep track of the execution order and return to the correct location after the function call is completed.

- Expression Evaluation: Stacks can be used to evaluate expressions, particularly infix expressions. Operators and operands are pushed onto the stack, and the operations are performed based on the order of the items in the stack.

- Undo/Redo Operations: Stacks are often used to implement undo and redo functionality in applications. Each action performed is stored on the stack, allowing users to reverse or redo their actions in a sequential manner.

- Browser History: Stacks are used to implement the back and forward navigation in web browsers. Each visited page is pushed onto the stack, enabling users to go back to previously visited pages by popping items from the stack.

## Big O Notation for Stack Data Structures

The notation O(1) indicates that an algorithm or operation has a constant time complexity. It means that regardless of the size of the input, the algorithm will always take the same amount of time to execute.

The notation O(n) indicates that an algorithm's time complexity grows linearly with the size of the input. It means that the running time of the algorithm increases proportionally with the input size.

The following table summarizes the time complexities for common operations in a Stacks:

| Operation           | Time Complexity |
|---------------------|-----------------|
| Push operation      | O(1)            |
| Pop Operation       | O(1)            |
| Search Operation    | O(n)            |
| Access Operation    | O(n)            |

## Implementation of Stack in Python
Now, let's implement a stack data structure in Python using a list. Python lists are dynamic arrays that can be easily used as stacks.



### Initializing a Stack
```python
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")

    def size(self):
        return len(self.stack)
```

In the above implementation, we define a Stack class that uses a list to store the elements. Here's a brief explanation of the methods:

- The **__init__** method initializes an empty stack.
- The **push** method adds an item to the top of the stack using the append method of the list.
- The **pop** method removes and returns the top element from the stack using the **pop** method of the list. It also checks if the stack is empty before performing the operation.
- The **peek** method returns the top element of the stack without removing it. It also checks if the stack is empty before performing the operation.
- The **is_empty** method checks if the stack is empty by checking the length of the list.
- The **size** method returns the number of elements in the stack by returning the length of the list.

### Using a Stack
```python
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())  # Output: 30
print(stack.pop())  # Output: 30
print(stack.size())  # Output: 2
print(stack.is_empty())  # Output: False
```
## Conclusion 

Stacks are versatile data structures with a wide range of applications. Stacks are useful when you need to maintain a Last-In-First-Out order of elements. They are commonly used in various algorithms and applications. Remember to consider the stack operations such as push, pop, peek, isEmpty, and size when working with stacks in Python.

## Home
-[Home Page](https://github.com/KurtHermansen/Data-Structures/blob/master/0-welcome.md)