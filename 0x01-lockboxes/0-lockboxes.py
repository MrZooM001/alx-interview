#!/usr/bin/python3
"""Module to implement an algorith to check boxes are unlocked."""
from collections import deque


def canUnlockAll(boxes):
    """
    Method that Checks if all the boxes in a list of lists can be unlocked.

    Args:
        boxes (list[list[int]]): A list where the keys are box numbers
        and the values are a list of keys that can unlock that box.

    Returns:
        bool: True if all the boxes can be unlocked, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    seen_boxes = {0}
    unseen_boxes = set(boxes[0]) - {0}

    while unseen_boxes:
        box = unseen_boxes.pop()
        if not (0 <= box < n):
            continue
        if box not in seen_boxes:
            unseen_boxes.update(boxes[box])
            seen_boxes.add(box)

    return len(seen_boxes) == n
