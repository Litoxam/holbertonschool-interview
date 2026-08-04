#!/usr/bin/python3


def validUTF8(data):
    """
    Returns True if data is a valid UTF-8 encoding.
    """

    bytes_left = 0

    for num in data:
        byte = num & 0xFF

    return True