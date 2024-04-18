#!/usr/bin/python3
"""Module to implement an algorith to check boxes are unlocked."""
from collections import deque


def canUnlockAll(boxes):
    """
    Method that Checks if all the boxes in a list of lists can be unlocked.

    Args:
        boxes (list): A list where the keys are box numbers
        and the values are a list of keys that can unlock that box.

    Returns:
        bool: True if all the boxes can be unlocked, False otherwise.
    """
    if not boxes:
        return False

    num_boxes = len(boxes)
    seen = set()
    seen.add(0)

    def depth_first(box):
        for key in boxes[box]:
            if key < num_boxes and key not in seen:
                seen.add(key)
                depth_first(key)

    depth_first(0)

    return len(seen) == num_boxes
