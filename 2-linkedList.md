# Linked List Data Structure

-[Home Page](https://github.com/KurtHermansen/Data-Structures/blob/master/0-welcome.md)

## Introduction
In this comprehensive Tutorial, we will explore the fascinating world of linked lists, a fundamental data structure in computer programming. Linked lists play a crucial role in many applications and algorithms, and understanding their concepts and operations is essential for any programmer or computer science enthusiast.

In programming, we often deal with collections of data that need to be stored, accessed, and manipulated efficiently. While arrays provide a straightforward way to store such data, they have certain limitations. Arrays require contiguous memory allocation, meaning that we need to reserve a block of memory large enough to accommodate the entire collection, even if the size of the collection may change over time. Additionally, inserting or deleting elements in an array can be time-consuming, especially if the array is large and the operation involves shifting multiple elements.

This is where linked lists come to the rescue! Linked lists offer a dynamic and efficient alternative to arrays. Unlike arrays, linked lists do not require contiguous memory allocation. Instead, they use a series of interconnected nodes, each containing the data element and a reference (or pointer) to the next node in the sequence. This dynamic memory allocation allows for more flexibility in managing data and performing insertion and deletion operations.

![Linked List Picture](https://github.com/KurtHermansen/Data-Structures/blob/master/linkedList.png)

## Anatomy of a Linked List
To understand linked lists better, let's take a closer look at their structure. A linked list is composed of nodes, and each node consists of two main components:

1. **Data:** This component stores the actual data element. It can be any value or object that needs to be stored within the linked list, such as integers, strings, or complex data structures.

2. **Next Pointer:** This component is a reference (or pointer) to the next node in the sequence. It points to the memory location where the next node is stored. This linking mechanism connects all the nodes together, forming the linked list.

At the start of the linked list, we have the **head** node, which serves as the entry point and allows us to access the entire list. The last node in the list is called the **tail** node and typically has its next pointer pointing to **null** or a special termination marker.

## Linked List Operations

### Insertion

Insertion is the process of adding a new node to the linked list at a specific position. There are different ways to insert a new node, such as at the beginning, at the end, or at a given position within the list.

- **Insertion at the Beginning:** The new node is added at the start of the linked list, and its next pointer is set to the previous head. This operation involves updating the head pointer to the new node.

- **Insertion at the End:** The new node is appended at the end of the linked list, and its next pointer is set to null. If the list is empty, the new node becomes the head.

- **Insertion at a Given Position:** The new node is inserted at a specific position within the linked list. This operation requires traversing the list to find the desired position and adjusting the pointers accordingly.

### Deletion

Deletion is the process of removing a node from the linked list. Similar to insertion, there are different ways to delete a node, such as deleting the first node, deleting the last node, or deleting a node at a given position.

- **Deletion of the First Node:** The first node in the linked list is removed, and the head pointer is updated to the next node.

- **Deletion of the Last Node:** The last node in the linked list is removed. This operation requires traversing the list to reach the second-to-last node and updating its next pointer to null.

- **Deletion of a Node at a Given Position:** A node at a specific position within the linked list is deleted. This operation involves traversing the list to find the desired position and adjusting the pointers of the surrounding nodes.

### Searching

Searching in a linked list involves finding a specific element or a node that matches certain criteria. To search for an element, you need to traverse the linked list, comparing the data in each node with the desired value. If a match is found, you can perform further operations on the node or return its position.

### Traversal

Traversal refers to the process of visiting each node in the linked list and performing some operation on it. By traversing the list, you can access and process the data stored in each node. Traversal is typically done using a loop, starting from the head and following the next pointers until reaching the end of the list.


## Pros and Cons
### Pros
- Dynamic Size: Linked lists can grow or shrink during runtime, as memory allocation is not fixed like in arrays. This flexibility makes them suitable for scenarios where the size of the data may vary.

- Efficient Insertion and Deletion: Insertion and deletion operations can be performed in constant time (O(1)) at the beginning or end of a linked list, assuming the position is known. This makes linked lists efficient for scenarios involving frequent data modification.

- No Contiguous Memory Requirement: Linked lists do not require contiguous memory allocation, unlike arrays. This property allows efficient memory utilization and eliminates the need to preallocate a fixed amount of memory.

### Cons
- Lack of Random Access: Unlike arrays, linked lists do not provide direct access to elements at arbitrary positions. To access an element, the list must be traversed from the head until the desired node is reached. This traversal requires linear time, resulting in a time complexity of O(n).

- Extra Memory Overhead: Linked lists require additional memory to store the references or links between nodes. This overhead can be significant when compared to arrays, where only the data elements are stored.

- Sequential Access: Linked lists are optimized for sequential access. Accessing elements at arbitrary positions or performing operations like searching requires traversing the list, resulting in increased time complexity.

## Use Cases
- Dynamic Data: Linked lists are suitable for scenarios where data size can change dynamically, such as implementing a queue or stack.

- Insertion and Deletion: Linked lists excel in situations where frequent insertions or deletions of elements are required, such as maintaining a sorted list or implementing an undo/redo functionality.

- Limited Memory: Linked lists are useful when memory is limited or needs to be efficiently utilized. Since linked lists do not require contiguous memory allocation, they can be more efficient than arrays in such cases.

## Big O Notation

The notation O(1) indicates that an algorithm or operation has a constant time complexity. It means that regardless of the size of the input, the algorithm will always take the same amount of time to execute.

The notation O(n) indicates that an algorithm's time complexity grows linearly with the size of the input. It means that the running time of the algorithm increases proportionally with the input size.

The following table summarizes the time complexities for common operations in a linked list:

| Operation     | Time Complexity |
|---------------|-----------------|
| Access        | O(n)            |
| Search        | O(n)            |
| Insertion     | O(1) or O(n)    |
| Deletion      | O(1) or O(n)    |

## Python Code Examples

### Node Class
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```
### Linked List Class
```python
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def insert_at_position(self, value, position):
        if position <= 0:
            self.insert_at_beginning(value)
        else:
            new_node = Node(value)
            current = self.head
            count = 0
            while current is not None and count < position - 1:
                current = current.next
                count += 1
            if current is None:
                print("Position out of range")
            else:
                new_node.next = current.next
                current.next = new_node

    def delete_at_beginning(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("List is empty")

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
    def delete_at_position(self, position):
        if position <= 0:
            self.delete_at_beginning()
        elif self.head is None:
            print("List is empty")
        else:
            current = self.head
            count = 0
            while current.next is not None and count < position - 1:
                current = current.next
                count += 1
            if current.next is None:
                print("Position out of range")
            else:
                current.next = current.next.next
    def search(self, value):
        current = self.head
        position = 0
        while current is not None:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1
    # Traversal
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
```
### Using a Linked List
```python

# Creating a new linked list
my_list = LinkedList()

# Inserting nodes at the beginning
my_list.insert_at_beginning(5)
my_list.insert_at_beginning(3)
my_list.insert_at_beginning(1)

# Inserting nodes at the end
my_list.insert_at_end(7)
my_list.insert_at_end(9)

# Inserting a node at a specific position
my_list.insert_at_position(6, 3)

# Displaying the linked list
print("Linked List after insertions:")
my_list.traverse()
# Expected output: 1 -> 3 -> 5 -> 6 -> 7 -> 9

# Deleting nodes
my_list.delete_at_beginning()
my_list.delete_at_end()
my_list.delete_at_position(2)

# Displaying the linked list after deletions
print("Linked List after deletions:")
my_list.traverse()
# Expected output: 3 -> 5 -> 7

# Searching for a value in the linked list
value = 7
position = my_list.search(value)
if position != -1:
    print(f"Value {value} found at position {position}")
else:
    print(f"Value {value} not found in the linked list")
# Expected output: Value 7 found at position 2
```

## Conclusion

Linked lists are versatile data structures that provide efficient insertion and deletion operations. They are particularly useful in scenarios where the data size is dynamic or frequent modifications are required. However, linked lists have limitations in terms of random access and additional memory overhead. Understanding the fundamentals of linked lists and their implementation in a programming language like Python can greatly enhance your ability to solve problems efficiently.

## Home
-[Home Page](https://github.com/KurtHermansen/Data-Structures/blob/master/0-welcome.md)