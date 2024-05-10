#include "sort.h"

/**
 * heap_sort - Sorts An Array Fllowing The Heap Sort Algorithm.
 *
 * @array: Array Of Integers Sort In Ascending Order.
 * @size: Size Of The Array To Sort.
 *
 * Return: Print The Array After Each Time You Swap Two Elements.
 */
void heap_sort(int *array, size_t size)
{
	int i;
	int tmp;

	if (size < 2)
		return;

	for (i = size / 2 - 1; i >= 0; i--)
		heapify(array, size, (size_t)i, size);

	for (i = size - 1; i >= 0; i--)
	{
		tmp = array[i];
		array[i] = array[0];
		array[0] = tmp;
		if (i != 0)
			print_array(array, size);
		heapify(array, (size_t)i, 0, size);
	}
}

/**
 * heapify - Turns An Array In A Heap Tree
 * @array: Array To Turn Into Heap
 * @s: Size Of The Subtree
 * @root: Index Of The Subtree In The Heap
 * @size: Size Of The Whole Array
 */
void heapify(int *array, size_t s, size_t root, size_t size)
{
	size_t max, left, right;
	int tmp;

	max = root;
	left = (root * 2) + 1;
	right = (root * 2) + 2;

	if (left < s && array[left] > array[max])
		max = left;

	if (right < s && array[right] > array[max])
		max = right;

	if (max != root)
	{
		tmp = array[root];
		array[root] = array[max];
		array[max] = tmp;
		print_array(array, size);
		heapify(array, s, max, size);
	}
}
