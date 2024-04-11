#include "binary_trees.h"
#include <stdlib.h>

/**
 * sorted_array_to_avl - builds an AVL tree from a sorted array
 * @array: sorted array to build the tree from
 * @size: size of the array
 *
 * Return: pointer to the root node of the created AVL tree, or NULL on failure
 */
avl_t *sorted_array_to_avl(int *array, size_t size)
{
    if (array == NULL || size == 0)
        return (NULL);

    return (recursive_tree(array, 0, size - 1));
}

/**
 * create_node - creates a new AVL node
 * @n: value to put in the new node
 *
 * Return: pointer to the new node, or NULL on failure
 */
avl_t *create_node(int n)
{
    avl_t *new_node = malloc(sizeof(avl_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = n;
    new_node->parent = NULL;
    new_node->left = NULL;
    new_node->right = NULL;

    return (new_node);
}

/**
 * recursive_tree - builds the AVL tree recursively
 * @array: sorted array to build the tree from
 * @start: starting index of the current subarray
 * @end: ending index of the current subarray
 *
 * Return: pointer to the root node of the created AVL tree, or NULL on failure
 */
avl_t *recursive_tree(int *array, size_t start, size_t end)
{
    if (start > end)
        return (NULL);

    size_t mid = start + (end - start) / 2;
    avl_t *parent = create_node(array[mid]);
    if (parent == NULL)
        return (NULL);

    parent->left = recursive_tree(array, start, mid - 1);
    if (parent->left != NULL)
        parent->left->parent = parent;

    parent->right = recursive_tree(array, mid + 1, end);
    if (parent->right != NULL)
        parent->right->parent = parent;

    return (parent);
}
