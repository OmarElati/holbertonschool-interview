#include "binary_trees.h"
#include <limits.h>

/**
 * is_bst_avl - Helper function to check if tree is a valid AVL tree
 * @tree: Pointer to the root node of the tree to check
 * @min: Minimum allowed value for the current node
 * @max: Maximum allowed value for the current node
 * @height: Pointer to the height of the current tree
 *
 * Return: 1 if tree is a valid AVL tree, 0 otherwise
 */
int is_bst_avl(const binary_tree_t *tree, int min, int max, int *height)
{
	int left_height = 0, right_height = 0;

	if (!tree)
	{
		*height = 0;
		return (1);
	}

	if (tree->n <= min || tree->n >= max)
		return (0);

	if (!is_bst_avl(tree->left, min, tree->n, &left_height) ||
		!is_bst_avl(tree->right, tree->n, max, &right_height))
		return (0);

	*height = (left_height > right_height ? left_height : right_height) + 1;

	return (abs(left_height - right_height) <= 1);
}

/**
 * binary_tree_is_avl - Checks if a binary tree is a valid AVL tree
 * @tree: Pointer to the root node of the tree to check
 *
 * Return: 1 if tree is a valid AVL Tree, 0 otherwise
 */
int binary_tree_is_avl(const binary_tree_t *tree)
{
	int height = 0;

	if (!tree)
		return (0);

	return (is_bst_avl(tree, INT_MIN, INT_MAX, &height));
}
