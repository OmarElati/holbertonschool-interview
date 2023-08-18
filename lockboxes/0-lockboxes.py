#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    total_boxes = len(boxes)
    unlocked_boxes = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box < total_boxes:
            for key in boxes[current_box]:
                if key not in unlocked_boxes:
                    unlocked_boxes.add(key)
                    stack.append(key)

    return len(unlocked_boxes) == total_boxes
