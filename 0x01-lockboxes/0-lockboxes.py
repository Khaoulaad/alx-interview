#!/usr/bin/python3
"""Represents a  module for working with lockboxes.
"""


def canUnlockAll(boxes):
    """Checking if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    """
    n = len(boxes)
    seenBoxes = set([0])
    unseenBoxes = set(boxes[0]).difference(set([0]))
    while len(unseenBoxes) > 0:
        boxIdx = unseenBoxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seenBoxes:
            unseenBoxes = unseenBoxes.union(boxes[boxIdx])
            seenBoxes.add(boxIdx)
    return n == len(seenBoxes)
