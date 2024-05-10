#include "sort.h"

/**
 * heap_sort - Sorts An Array Using The Heap Sort Algorithm.
 *
 * @array: Array Of Integers To Sort.
 * @size: Size Of The Array To Sort.
 */
void heap_sort(int *array, size_t size)
{
	if (size < 2)
		return;

	for (int i = size / 2 - 1; i >= 0; i--)
		heapify(array, size, i);

	for (int i = size - 1; i > 0; i--)
	{
		int tmp = array[0];

		array[0] = array[i];
		array[i] = tmp;

		heapify(array, i, 0);
		print_array(array, size);
	}
}

/**
 * heapify - To Heapify Subtree Rooted With Node i Which Is An Index In Array.
 *
 * @array: Array To Heapify.
 * @n: Size Of Heap.
 * @i: Index Of Node To Heapify.
 */
void heapify(int *array, size_t n, int i)
{
	int largest = i;
	int l = 2 * i + 1;
	int r = 2 * i + 2;

	if (l < n && array[l] > array[largest])
		largest = l;

	if (r < n && array[r] > array[largest])
		largest = r;

	if (largest != i)
	{
		int tmp = array[i];

		array[i] = array[largest];
		array[largest] = tmp;

		heapify(array, n, largest);
	}
}
