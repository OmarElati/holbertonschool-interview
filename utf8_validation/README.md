## validate_utf8.py

This module contains a method for determining if a given data set represents a valid UTF-8 encoding.

### Usage

```python
from validate_utf8 import validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
```

- Output:

True
True
False


### Explanation

The `validUTF8()` method takes a list of integers representing the bytes of a UTF-8 encoded string. The method returns `True` if the data is a valid UTF-8 encoding, else `False`.

The method works by iterating over the bytes in the data set. For each byte, the method determines if the byte is the first byte of a character, a continuation byte, or an invalid byte. If the byte is the first byte of a character, the method determines the number of bytes in the character. If the byte is a continuation byte, the method decrements the number of bytes remaining in the character. If the byte is an invalid byte, the method returns `False`.

The method returns `True` if the number of bytes remaining in the last character is 0, else `False`.

### Example

The following is an example of how to use the `validUTF8()` method to validate a UTF-8 encoded string:

```python
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]

if validUTF8(data):
  print("The data is a valid UTF-8 encoding.")
else:
  print("The data is not a valid UTF-8 encoding.")
```

- This will print the following to the console:
    The data is a valid UTF-8 encoding.
