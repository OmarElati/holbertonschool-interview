# Sorted Array to AVL Tree

This C program converts a sorted array into an AVL tree. It includes functions to print binary trees for visualization.

## Overview

The program takes a sorted array of integers and constructs a balanced AVL tree from it. It then provides a function to print the resulting AVL tree in a visual format, allowing easy visualization of the tree's structure.

## Code Structure

The main components of the program are:

1. **binary_trees.h**: Header file containing structure definitions and function prototypes for binary trees.

2. **0-sorted_array_to_avl.c**: Source file containing the implementation of the function to convert a sorted array to an AVL tree.

3. **binary_tree_print.c**: Source file containing functions to print binary trees for visualization purposes.

4. **0-main.c**: Source file containing the main function to test the functionality of the program.

## How to Use

To build and run the program:

1. Clone this repository to your local machine.
2. Compile the code using the provided Makefile or GCC command.
3. Execute the compiled program to see the AVL tree constructed from the sorted array.

Example usage:

```bash
$ gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 0-main.c 0-sorted_array_to_avl.c -o 0-sorted_array_to_avl
$ ./0-sorted_array_to_avl
```

## Functions

### sorted_array_to_avl

```c
avl_t *sorted_array_to_avl(int *array, size_t size);
```

This function takes a sorted array of integers and the size of the array as input and constructs an AVL tree from it. It returns a pointer to the root node of the created AVL tree.

### binary_tree_print

```c
void binary_tree_print(const binary_tree_t *tree);
```

This function prints a binary tree in a visual format. It takes a pointer to the root node of the tree as input and prints the tree's structure to the standard output.

### Usage

To use the program, include the necessary header file (binary_trees.h) and call the sorted_array_to_avl function with a sorted array of integers to construct an AVL tree. You can then use the binary_tree_print function to visualize the resulting tree.

Example usage:

```c
#include <stdio.h>
#include "binary_trees.h"

int main(void)
{
    avl_t *tree;
    int array[] = {1, 2, 3, 4, 5};
    size_t size = sizeof(array) / sizeof(array[0]);

    tree = sorted_array_to_avl(array, size);
    if (!tree)
    {
        fprintf(stderr, "Failed to create AVL tree\n");
        return (1);
    }

    binary_tree_print(tree);

    return (0);
}
```

## Credits

- Original code for printing binary trees was adapted from [stackoverflow](http://stackoverflow.com/a/13755911/5184480).
