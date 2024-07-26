# Radix Sort
This project implements the Radix Sort algorithm in C, following the Least Significant Digit (LSD) method. The goal is to sort an array of integers in ascending order. The project adheres to specific coding standards and constraints.

## Requirements

- **Editors**: vi, vim, emacs
- **OS**: Ubuntu 14.04 LTS
- **Compiler**: gcc 4.8.4 with flags `-Wall -Werror -Wextra -pedantic`
- **Code Style**: Betty style
- **Global Variables**: Not allowed
- **Function Limit**: No more than 5 functions per file
- **Standard Library**: Not allowed (except for `malloc` and `free`)
- **Project Files**:
  - `0-radix_sort.c`: Implementation of the Radix Sort algorithm
  - `print_array.c`: Provided function to print arrays
  - `sort.h`: Header file with function prototypes
  - `README.md`: This documentation file

## Usage

1. **Clone the repository**:
```sh
git clone https://github.com/your_username/holbertonschool-interview.git
cd holbertonschool-interview/radix_sort
```

2. **Compile the code**:
```sh
Copier le code
gcc -Wall -Wextra -Werror -pedantic 0-main.c 0-radix_sort.c print_array.c -o radix
```

3. **Run the executable**:
```sh
./radix
```

## Function Descriptions
```c
radix_sort(int *array, size_t size)
```
Sorts an array of integers using the Radix Sort algorithm.
```c
print_array(const int *array, size_t size)
```
Prints an array of integers.

## Example

Input array: `19, 48, 99, 71, 13, 52, 96, 73, 86, 7`

Output (after sorting): `7, 13, 19, 48, 52, 71, 73, 86, 96, 99`

## File Descriptions

- **[0-radix_sort.c](./0-radix_sort.c)**: Contains the implementation of the Radix Sort algorithm.
- **[print_array.c](./print_array.c)**: Contains the print_array function, used to print arrays.
- **[sort.h](./sort.h)**: Contains the function prototypes for the functions used in this project.
- **[0-main.c](./0-main.c)**: A sample main file used for testing the implementation.
