#!/usr/bin/python3
"""Module to represent UTF-8 validation."""


def validUTF8(data):
    """
    Function to determine if a given data set represents a valid UTF-8 encoding

    Arguments:
        data (List[int]): A list of integers representing the byte array.

    Returns:
        bool: True if the byte array represents
        a valid UTF-8 encoded string, False otherwise.
    """
    num_bytes = 0
    shift1 = 1 << 7
    shift2 = 1 << 6

    for byte in data:
        if num_bytes == 0:
            shift = 1 << 7
            while shift & byte:
                num_bytes += 1
                shift = shift >> 1
            if num_bytes == 0:
                continue
            if num_bytes > 4 or num_bytes == 1:
                return False
        else:
            if not (byte & shift1 and not (byte & shift2)):
                return False
        num_bytes -= 1
    if num_bytes:
        return False

    return True
