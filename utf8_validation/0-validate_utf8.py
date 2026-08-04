#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Returns True if data is a valid UTF-8 encoding.
    """

    bytes_left = 0

    for num in data:
        # Keep only the last 8 bits
        byte = num & 0xFF

        if bytes_left == 0:
            # 1-byte character: 0xxxxxxx
            if (byte >> 7) == 0:
                continue

            # 2-byte character: 110xxxxx
            elif (byte >> 5) == 0b110:
                bytes_left = 1

            # 3-byte character: 1110xxxx
            elif (byte >> 4) == 0b1110:
                bytes_left = 2

            # 4-byte character: 11110xxx
            elif (byte >> 3) == 0b11110:
                bytes_left = 3

            # Invalid UTF-8 starting byte
            else:
                return False

        else:
            # Continuation bytes must start with 10
            if (byte >> 6) != 0b10:
                return False

            bytes_left -= 1

    # All characters must be complete
    if bytes_left == 0:
        return True
    else:
        return False
