#!/usr/bin/python3
"""UTF-8 Encoding"""


def validUTF8(data):
    """
        A function that takes data as an argument and tests it to ensure that
        its a valid UTF-8 encoding
    """
    try:
        joined_data = bytes(data)
        joined_data.decode('utf-8')
        return True
    except (UnicodeDecodeError, ValueError) as e:
        return False
