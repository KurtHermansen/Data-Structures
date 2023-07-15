# Tree Data Structure

-[Home Page](https://github.com/KurtHermansen/Data-Structures/blob/master/0-welcome.md)

## Introduction
A tree data structure is a fundamental concept in computer science and plays a crucial role in various algorithms and applications. It provides a way to organize and represent hierarchical relationships between elements, making it a powerful tool for solving complex problems. In this tutorial, we will delve into the world of trees, terminology, implementation, and traversal techniques using Python.

Trees are widely used in many areas of computer science, including data storage and retrieval, network routing algorithms, decision-making processes, and more. Understanding trees and their operations is essential for any programmer or data scientist who deals with hierarchical structures or needs to optimize algorithms for efficiency.

This tutorial aims to provide you with a comprehensive understanding of trees, starting from the basics and gradually moving towards more advanced concepts. Whether you are new to trees or already have some experience, this tutorial will help you solidify your knowledge and develop the skills to work with trees effectively.

A tree is a collection of nodes connected by edges. It is a non-linear data structure that represents a hierarchical relationship between elements. A tree consists of a root node and zero or more child nodes. Each child node can have its own children, forming a hierarchical structure.

![Tree Picture](https://github.com/KurtHermansen/Data-Structures/blob/master/tree.png)

## Tree Terminology

Here are the key terminologies used in the context of trees:

To keep things simple we will focus on **Binary trees** only. A binary tree is a tree in which each node can have at most two children, referred to as the left child and the right child.

- **Node:** A node represents an element in a tree. It contains a value or payload and may also include additional attributes or references.

- **Root:** The root is the topmost node in a tree. It serves as the starting point for accessing other nodes in the tree. There is only one root node in a tree.

- **Child:** A child node is a node that has a parent node. In a tree, each node (except the root) has exactly one parent. A parent can have multiple child nodes.

- **Parent:** A parent node is a node that has one or more child nodes. It is the immediate predecessor of its child nodes.

- **Sibling:** Sibling nodes are nodes that have the same parent. They share a common parent node.

- **Leaf:** A leaf node, also known as a terminal node or external node, is a node that does not have any child nodes. In other words, it is a node that resides at the end of a branch.

- **Edge:** An edge is a connection between two nodes in a tree. It represents the link or relationship between nodes.

## Tree Operations

### Insertion

Insertion involves adding a new node to the tree. The node can be inserted at a specific position based on the desired tree structure.

### Deletion

Deletion involves removing a node from the tree while maintaining the tree's structure and properties. The deletion process can vary depending on the type of tree.

### Search

Searching involves finding a specific value or node in the tree.

### Traversal

Traversal refers to visiting each node in the tree in a specific order. There are different traversal techniques, including depth-first and breadth-first traversal.

### Finding Min and Max

Finding Minimum/Maximum: Finding the minimum or maximum value in a tree involves locating the leftmost or rightmost node in the tree, respectively. 

## Pros and Cons
Pros:
- Provides a hierarchical structure for organizing and representing data.
- Efficient for organizing and searching data that has a hierarchical nature.
- Supports efficient insertion, deletion, and retrieval operations.
- Enables various tree-based algorithms like binary search and tree traversals.

Cons:
- Requires additional memory for storing child links, which can increase memory overhead.
- Insertion and deletion operations can be complex and time-consuming.
- Tree structure manipulation can be challenging to implement and debug.

## Use Cases
1. File Systems: Trees are used to represent the hierarchical structure of files and directories in an operating system's file system.

2. Organization Charts: Trees are employed to represent the hierarchical structure of an organization, including departments, sub-departments, and employees.

3. Family Trees: Trees are used to represent genealogical relationships in family trees, including ancestors, descendants, and their connections.

5. Decision Trees: Trees are used in machine learning algorithms, such as decision trees, for classification and regression tasks.

6. HTML/XML Parsing: Trees are used to parse and represent the structure of HTML or XML documents for manipulation or extraction of data.


## Big O Notation

The notation O(n) indicates that an algorithm's time complexity grows linearly with the size of the input. It means that the running time of the algorithm increases proportionally with the input size.

The notation O(log n) represents logarithmic time complexity. It means that the algorithm's runtime grows logarithmically with the input size. As the input size increases, the runtime of the algorithm increases at a slower rate compared to linear time complexity.

The time complexity of basic tree operations in the average and worst cases **Note:** that these complexities are specific to binary trees, and the actual time complexities may vary depending on the type of tree and its properties.

| Operation     | Average Complexity | Worst Complexity |
|---------------|--------------------|------------------|
| Insertion     | O(log n)           | O(n)             |
| Deletion      | O(log n)           | O(n)             |
| Search        | O(log n)           | O(n)             |
| Traversal     | O(n)               | O(n)             |

## Python Code Examples
Here are a few examples of using trees in Python:

### Implementing a basic binary tree
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### Tree Operations
```python
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
```


### Using a Tree

```python
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
```
## Tree Structure

The binary search tree created in the previous test would look like this:
```python
        50
       /  \
     30    70
    /  \   / \
   20  40 60  80
   ```

## Conclusion

Trees are powerful data structures that provide hierarchical organization and efficient access to elements. They play a vital role in algorithm design, data representation, and solving complex problems. By understanding and implementing trees in Python, you have gained a valuable skill set that can be applied to various domains, such as data analysis, graph algorithms, and decision-making processes.

## Home
-[Home Page](https://github.com/KurtHermansen/Data-Structures/blob/master/0-welcome.md)