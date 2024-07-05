#ifndef _SORT_H_
#define _SORT_H_

/* INCLUDED LIBRARIES */
#include <stdlib.h>
#include <stdio.h>

/* FUNCTION PROTOTYPES */
void print_array(const int *array, size_t size);
void merge_sort(int *array, size_t size);
void merge(int *array, int *temp, size_t left, size_t mid, size_t right);
void merge_sort_recursive(int *array, int *temp, size_t left, size_t right);

#endif /* _SORT_H_ */

