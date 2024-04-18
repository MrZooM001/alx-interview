#!/usr/bin/python3
"""Module to implement Pascal's Triangle."""
from collections import deque


def canUnlockAll(boxes):
    """
    Method that Checks if all the boxes in a dictionary can be unlocked.

    Parameters:
        boxes (dict): A dictionary where the keys are box numbers and the values are a list of keys that can unlock that box.

    Returns:
        bool: True if all the boxes can be unlocked, False otherwise.
    """
    if not boxes:
        return False

    num_boxes = len(boxes)
    seen = set()  # Set to keep track of boxes we have seen
    queue = deque([0])  # Queue to keep track of boxes we can currently unlock

    while queue:
        box = queue.popleft()
        seen.add(box)  # Mark the current box as seen

        for key in boxes[box]:
            if key < num_boxes and key not in seen:
                queue.append(key)

    return len(seen) == num_boxes
