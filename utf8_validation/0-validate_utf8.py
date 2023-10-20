#!/usr/bin/python3
"""
method that determines if a given data
set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set
    represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing
        the bytes of a UTF-8 encoded string.

    Returns:
        True if data is a valid UTF-8 encoding,
        else return False.
    """
    for byte in data:
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                num_bytes = 0
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                num_bytes -= 1
            else:
                return False

    return num_bytes == 0
