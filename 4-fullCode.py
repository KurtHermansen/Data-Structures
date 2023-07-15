#Stack code and Tests
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
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("\n=========== STACK TESTS ===========")
print(stack.peek())  # Output: 30
print(stack.pop())  # Output: 30
print(stack.size())  # Output: 2
print(stack.is_empty())  # Output: False
print("\n=========== STACK TESTS END ===========")


# Linked List code and tests
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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
print("\n=========== LINKED LIST TESTS ===========")
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
print("\n=========== LINKED LIST TESTS END ===========")


##Tree Data Structure

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    elif value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root

def delete_node(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            min_node = find_min(root.right)
            root.value = min_node.value
            root.right = delete_node(root.right, min_node.value)

    return root

def search_value(root, value):
    if root is None or root.value == value:
        return root

    if value < root.value:
        return search_value(root.left, value)
    else:
        return search_value(root.right, value)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)

def find_min(root):
    if root.left is None:
        return root
    return find_min(root.left)


# Test Tree Operations

# Create an empty tree
tree = None

# Insert nodes
tree = insert_node(tree, 50)
tree = insert_node(tree, 30)
tree = insert_node(tree, 70)
tree = insert_node(tree, 20)
tree = insert_node(tree, 40)
tree = insert_node(tree, 60)
tree = insert_node(tree, 80)

# Expected Output (inorder traversal): 20, 30, 40, 50, 60, 70, 80
print("Inorder Traversal:")
inorder_traversal(tree)
print()

# Search for a value
search_value_result = search_value(tree, 60)

# Expected Output: Node with value 60 exists in the tree
print("Search Value Result:")
print(search_value_result)
print()

# Delete a node
tree = delete_node(tree, 30)

# Expected Output (inorder traversal): 20, 40, 50, 60, 70, 80
print("Inorder Traversal after Deleting Node with Value 30:")
inorder_traversal(tree)
print()

# Find the minimum value
min_value = find_min(tree)

# Expected Output: Minimum value in the tree: 20
print("Minimum Value:")
print(min_value.value)
