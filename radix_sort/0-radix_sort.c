#include "sort.h"

/**
 * get_max - Find the maximum number in an array
 * @array: The array of integers
 * @size: The size of the array
 * Return: The maximum number in the array
 */
int get_max(int *array, size_t size)
{
    int max = array[0];
    size_t i;
    for (i = 1; i < size; i++)
    {
        if (array[i] > max)
            max = array[i];
    }
    return max;
}

/**
 * counting_sort - Sort the array using counting sort based on the digit
 * @array: The array of integers
 * @size: The size of the array
 * @exp: The exponent representing the digit position
 */
void counting_sort(int *array, size_t size, int exp)
{
    int *output = malloc(size * sizeof(int));
    int count[10] = {0};
    size_t i;
    int digit;

    for (i = 0; i < size; i++)
        count[(array[i] / exp) % 10]++;

    for (digit = 1; digit < 10; digit++)
        count[digit] += count[digit - 1];

    for (i = size - 1; (int)i >= 0; i--)
    {
        output[count[(array[i] / exp) % 10] - 1] = array[i];
        count[(array[i] / exp) % 10]--;
    }

    for (i = 0; i < size; i++)
        array[i] = output[i];

    free(output);
}

/**
 * radix_sort - Sort an array of integers using radix sort algorithm
 * @array: The array to be sorted
 * @size: The size of the array
 */
void radix_sort(int *array, size_t size)
{
    if (size < 2)
        return;

    int max = get_max(array, size);
    int exp;

    for (exp = 1; max / exp > 0; exp *= 10)
    {
        counting_sort(array, size, exp);
        print_array(array, size);
    }
}
