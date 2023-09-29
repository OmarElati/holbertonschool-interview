#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int length = 0;
    int i = 0;
    int elements[i];

    while (current != NULL)
    {
        elements[length++] = current->n;
        current = current->next;
    }

    for (i = 0; i < length / 2; i++)
    {
        if (elements[i] != elements[length - 1 - i])
        {
            return 0;
        }
    }

    return 1;
}
