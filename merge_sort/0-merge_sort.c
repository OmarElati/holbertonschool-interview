#include "sort.h"

/**
 * merge_sort - Sorts an array of integers in ascending order
 *              using the Merge Sort algorithm.
 * @array: The array to be sorted.
 * @size: The size of the array.
 */
void merge_sort(int *array, size_t size)
{
	int *temp;

	if (array == NULL || size < 2)
		return;

	temp = malloc(sizeof(int) * size);
	if (temp == NULL)
		return;

	merge_sort_recursive(array, temp, 0, size - 1);

	free(temp);
}

/**
 * merge_sort_recursive - Recursively divides and sorts the array.
 * @array: The array to be sorted.
 * @temp: Temporary array for merging.
 * @left: The starting index of the left subarray.
 * @right: The ending index of the right subarray.
 */
void merge_sort_recursive(int *array, int *temp, size_t left, size_t right)
{
	size_t mid;

	if (left >= right)
		return;

	mid = left + (right - left) / 2;

	merge_sort_recursive(array, temp, left, mid);
	merge_sort_recursive(array, temp, mid + 1, right);
	merge(array, temp, left, mid, right);
}

/**
 * merge - Merges two sorted subarrays into a single sorted array.
 * @array: The array containing the subarrays to merge.
 * @temp: Temporary array for merging.
 * @left: The starting index of the left subarray.
 * @mid: The ending index of the left subarray and the starting index of the right subarray.
 * @right: The ending index of the right subarray.
 */
void merge(int *array, int *temp, size_t left, size_t mid, size_t right)
{
	size_t i = left, j = mid + 1, k = left;

	printf("Merging...\n[left]: ");
	print_array(array + left, mid - left + 1);
	printf("[right]: ");
	print_array(array + j, right - mid);

	while (i <= mid && j <= right)
	{
		if (array[i] <= array[j])
			temp[k++] = array[i++];
		else
			temp[k++] = array[j++];
	}

	while (i <= mid)
		temp[k++] = array[i++];

	while (j <= right)
		temp[k++] = array[j++];

	for (i = left; i <= right; i++)
		array[i] = temp[i];

	printf("[Done]: ");
	print_array(array + left, right - left + 1);
}
