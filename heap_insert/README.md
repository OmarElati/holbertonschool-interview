# Binary Tree Node Creation
This is a simple C program that demonstrates how to create and use binary tree nodes. The program provides a function binary_tree_node for creating binary tree nodes.

## Table of Contents
* Getting Started
* Prerequisites
* Installation
* Usage
* Contributing
* License
## Getting Started
Binary trees are a fundamental data structure in computer science. They consist of nodes, where each node has a value and optionally points to two child nodes, often referred to as the left child and the right child.

This project provides a simple function, binary_tree_node, which creates a binary tree node. Each node has a parent pointer, value, and pointers to its left and right children.

## Prerequisites
Before you can use this program, make sure you have the following installed:

GCC Compiler: You need a C compiler to compile and run the program.
## Installation
1. Clone the repository to your local machine:

``` shell
git clone https://github.com/your-username/binary-tree-node-creation.git
```
2. Compile the program using GCC:

``` shell
gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 0-main.c 0-binary_tree_node.c -o binary_tree_node
```

## Usage
To use the binary_tree_node function, follow these steps:

1. Include the binary_trees.h header file in your C source code:

``` c
#include "binary_trees.h"
```

2. Create a binary tree node by calling the binary_tree_node function and passing the parent node and the value for the new node:

``` c
binary_tree_t *new_node = binary_tree_node(parent, value);
```
* parent: A pointer to the parent node. Pass NULL if the new node has no parent.
* value: The value to store in the new node.
3. Use the new_node pointer to access and manipulate the binary tree node as needed.

4. Don't forget to deallocate memory when you're done to avoid memory leaks:

``` c
_binary_tree_delete(root);
```

## Contributing
If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

3. Create a new branch for your feature or bug fix.

4. Make your changes and test them thoroughly.

5. Commit your changes and push them to your GitHub repository.

6. Create a pull request to the original repository, describing your changes in detail.

7. Wait for feedback and approval from the maintainers.

## License
This project is licensed under the MIT License - see the LICENSE file for details.