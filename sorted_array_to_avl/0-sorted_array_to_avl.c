#include "binary_trees.h"

/**
 * sorted_array_to_avl - builds an AVL tree from a sorted array
 * @array: sorted array to build the tree from
 * @size: size of the array
 *
 * Return: pointer to the root node of the created AVL tree, or NULL on failure
 */
avl_t *sorted_array_to_avl(int *array, size_t size)
{
	avl_t *tree = NULL;

	if (!array || size == 0)
		return (NULL);

	tree = recursive_tree(array, 0, (int)size - 1);
	if (!tree)
		return (NULL);
	return (tree);
}

/**
 * create_node - creates a new AVL node
 * @n: value to put in the new node
 *
 * Return: pointer to the new node, or NULL on failure
 */
avl_t *create_node(int n)
{
	avl_t *node = NULL;

	node = malloc(sizeof(avl_t));
	if (!node)
		return (NULL);
	node->parent = NULL;
	node->left = NULL;
	node->right = NULL;
	node->n = n;
	return (node);
}

/**
 * recursive_tree - builds the AVL tree recursively
 * @array: array of integers
 * @start: starting index
 * @end: ending index
 * Return: pointer to the root node of the created AVL tree, or NULL on failure
 */
avl_t *recursive_tree(int *array, int start, int end)
{
	avl_t *left = NULL, *right = NULL, *parent = NULL;
	size_t n = 0;

	if (start > end)
		return (NULL);

	n = (start + end) / 2;
	left = recursive_tree(array, start, n - 1);
	right = recursive_tree(array, n + 1, end);

	parent = create_node(array[n]);
	if (!parent)
		return (NULL);

	if (left)
	{
		parent->left = left;
		left->parent = parent;
	}

	if (right)
	{
		parent->right = right;
		right->parent = parent;
	}

	return (parent);
}
