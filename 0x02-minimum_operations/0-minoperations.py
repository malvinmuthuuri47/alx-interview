#!/usr/bin/python3
"""
A module that computes the Minimum Operations needed to perform
a copy and paste functionality within a text editor
"""


def minOperations(n):
    """
        This function accepts n and calculates the number of total
        minimum operations needed to achieve the copy and paste
        functionality

        Args:
            n - The total number of characters that are going to be
                present in the text file after all the operations
                are completed

        Returns:
            The minimum total number of operations needed to complete
            the actions
    """
    len_h = 1
    len_copied_h = 0
    total_operations = 0

    if not isinstance(n, int):
        return 0

    while len_h < n:
        if n % len_h == 0:
            total_operations += 2
            len_copied_h = len_h
        else:
            total_operations += 1
        len_h += len_copied_h
    return total_operations
