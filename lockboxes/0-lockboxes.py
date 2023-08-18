#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    total_boxes = set([0])
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in total_boxes:
                total_boxes.add(key)
                queue.append(key)

    return len(total_boxes) == len(boxes)
