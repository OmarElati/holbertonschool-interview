# Palindrome integer

This C program checks whether a given unsigned integer is a palindrome or not. A palindrome is a number that reads the same backward as forward.

## Usage

1. Compile the C program using a C compiler, such as GCC:

```bash
gcc -Wall -Wextra -Werror -pedantic -g3 -o palindrome 0-main.c 0-is_palindrome.c
```

2. Run the compiled program, providing the number you want to check as an argument:

```bash
./palindrome_checker number
```

3. The program will output whether the provided number is a palindrome or not.

## Example

```
$ ./palindrome 1
1 is a palindrome.
$ ./palindrome 11
11 is a palindrome.
$ ./palindrome 112
112 is not a palindrome.
$ ./palindrome 121
121 is a palindrome.
$ ./palindrome 12345678987654321
12345678987654321 is a palindrome.
$ ./palindrome 123456789987654321
123456789987654321 is a palindrome.
$ ./palindrome 1234567898654321
1234567898654321 is not a palindrome.
```