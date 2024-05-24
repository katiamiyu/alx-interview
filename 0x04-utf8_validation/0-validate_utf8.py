#!/usr/bin/python3
""" Module UTF-8 Validation """


def validUTF8(data):
    """
    determines if a given data set represents a valid
    UTF-8 encoding.
    """
    number_bytes = 0

    mask_one = 1 << 7
    mask_two = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_one and not (i & mask_two)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
