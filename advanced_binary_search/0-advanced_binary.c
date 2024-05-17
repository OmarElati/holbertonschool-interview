#include "search_algos.h"
#include <stdio.h>

/**
 * print_subarray - Prints a subarray of integers
 * @array: Pointer to the first element of the subarray
 * @start: Index of the start of the subarray
 * @end: Index of the end of the subarray
 */
void print_subarray(int *array, size_t start, size_t end)
{
	size_t i;

	printf("Searching in array: ");
	for (i = start; i <= end; i++)
	{
		printf("%d", array[i]);
		if (i < end)
			printf(", ");
	}
	printf("\n");
}

/**
 * advanced_binary_recursive - Recursive function to perform advanced
 *										binary search
 * @array: Pointer to the first element of the array to search in
 * @start: Index of the start of the subarray
 * @end: Index of the end of the subarray
 * @value: Value to search for
 *
 * Return: Index where value is located, or -1 if not found
 */
int advanced_binary_recursive(int *array, size_t start, size_t end, int value)
{
	size_t mid;

	if (start > end)
		return (-1);

	print_subarray(array, start, end);

	mid = (start + end) / 2;

	if (array[mid] == value)
	{
		if (mid == 0 || array[mid - 1] != value)
			return (mid);
		else
			return (advanced_binary_recursive(array, start, mid, value));
	}
	else if (array[mid] < value)
		return (advanced_binary_recursive(array, mid + 1, end, value));
	else
		return (advanced_binary_recursive(array, start, mid - 1, value));
}

/**
 * advanced_binary - Searches for a value in a sorted array of integers
 * @array: Pointer to the first element of the array to search in
 * @size: Number of elements in array
 * @value: Value to search for
 *
 * Return: Index where value is located, or -1 if not found
 */
int advanced_binary(int *array, size_t size, int value)
{
	if (array == NULL || size == 0)
	{
		return (-1);
	}

	return (advanced_binary_recursive(array, 0, size - 1, value));
}
