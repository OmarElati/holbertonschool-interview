#include "search.h"

/**
 * linear_skip - searches for a value in a sorted skip list of integers
 * @list: pointer to the head of the skip list to search in
 * @value: value to search for
 * Return: pointer to the first node where value is located, or NULL if not found
 */
skiplist_t *linear_skip(skiplist_t *list, int value)
{
    skiplist_t *curr, *prev;

    if (list == NULL)
        return (NULL);

    curr = list;
    while (curr)
    {
        printf("Value checked at index [%lu] = [%d]\n", curr->index, curr->n);
        if (curr->express == NULL || curr->express->n >= value)
        {
            if (curr->n == value)
                return (curr);
            printf("Value found between indexes [%lu] and [%lu]\n",
                   curr->index, curr->express ? curr->express->index : curr->index);
            prev = curr;
            while (prev)
            {
                printf("Value checked at index [%lu] = [%d]\n", prev->index, prev->n);
                if (prev->n == value)
                    return (prev);
                if (prev->n > value)
                    return (NULL);
                prev = prev->next;
            }
        }
        curr = curr->express;
    }

    return (NULL);
}
