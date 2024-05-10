#ifndef SORT_H
#define SORT_H

#include <stdlib.h>
#include <stdio.h>

void print_array(const int *array, size_t size);
void heap_sort(int *array, size_t size);
void heapify(int *array, size_t s, size_t root, size_t size);
// Test Part
void quick_sort(int *array, size_t size);
void quicksort_recursive(int *array, int low, int high, size_t size);
int partition(int *array, int low, int high);

#endif /* SORT_H */
