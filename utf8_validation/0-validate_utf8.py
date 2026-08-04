#!/usr/bin/python3


def validUTF8(data):
    """
    Returns True if data is a valid UTF-8 encoding.
    """

    bytes_left = 0

    for num in data:
        byte = num & 0xFF

        if bytes_left == 0:

            if (byte >> 7) == 0:
                continue

            elif (byte >> 5) == 0b110:
                bytes_left = 1

            elif (byte >> 4) == 0b1110:
                bytes_left = 2

            elif (byte >> 3) == 0b11110:
                bytes_left = 3

            else:
                return False

        else:
        if (byte >> 6) != 0b10:
            return False

        bytes_left -= 1
        
    return True