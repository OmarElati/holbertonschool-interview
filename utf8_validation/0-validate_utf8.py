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

    num_bytes = 0
    binaryMoveLeft7 = 1 << 7
    binaryMoveLeft6 = 1 << 6
    for byte in data:
        binaryMove = 1 << 7
        if num_bytes == 0:
            while byte & binaryMove:
                num_bytes += 1
                binaryMove = binaryMove >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & binaryMoveLeft7 and not (byte & binaryMoveLeft6)):
                return False
        num_bytes -= 1
    if num_bytes == 0:
        return True
    return False
