#include "regex.h"

/**
 * regex_match - Check if the string matches the pattern.
 * @str: The input string.
 * @pattern: The regex pattern.
 *
 * Return: 1 if it matches, 0 otherwise.
*/

int regex_match(char const *str, char const *pattern)
{
	int dot = 0;
	int asterisk = 0;

	if (!str || !pattern)
		return (0);

	dot = *str && (*str == *pattern || *pattern == '.');
	asterisk = *(pattern + 1) == '*';

	if (!*str && !asterisk)
		return (*pattern ? 0 : 1);
	else if (dot && asterisk)
		return (regex_match(str + 1, pattern) || regex_match(str, pattern + 2));
	else if (dot && !asterisk)
		return (regex_match(str + 1, pattern + 1));
	else if (asterisk)
		return (regex_match(str, pattern + 2));
	return (0);
}
