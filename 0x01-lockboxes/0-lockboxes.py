#!/usr/bin/python3
"""
    Module to implement the LockBox problem
"""


def canUnlockAll(boxes):
    """
        Function to solve the lockbox problem

        @Args:
            boxes: A list of lists
    """
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
