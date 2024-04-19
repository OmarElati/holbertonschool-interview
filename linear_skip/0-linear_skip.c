#include "search.h"

/**
 * search_skip - search for a value between two nodes
 * @ben: starting node
 * @end: ending node
 * @value: value to search
 * Return: pointer to the node containing the value, or NULL if not found
 */
skiplist_t *search_skip(skiplist_t *ben, skiplist_t *end, int value)
{
	printf("Value found between indexes [%li] and [%li]\n",
		ben->index, end->index);
	while (ben != end->next)
	{
		printf("Value checked at index [%li] = [%i]\n", ben->index, ben->n);
		if (value == ben->n)
			return (ben);
		ben = ben->next;
	}
	return (NULL);
}

/**
 * linear_skip - search for a number in a linear skip list
 * @head: pointer to the head of the skip list
 * @value: value to search for
 * Return: pointer to the node containing the value, or NULL if not found
 */
skiplist_t *linear_skip(skiplist_t *head, int value)
{
	skiplist_t *ben, *end;

	if (!head)
		return (NULL);

	end = head;
	while (end && end->next && end->n < value)
	{
		ben = end;
		if (!end->express)
		{
			while (end->next)
				end = end->next;
			continue;
		}
		else
			end = end->express;
		printf("Value checked at index [%li] = [%i]\n", end->index, end->n);
	}
	return (search_skip(ben, end, value));
}
