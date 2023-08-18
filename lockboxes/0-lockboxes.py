#!/usr/bin/python3

def canUnlockAll(boxes):
    total_boxes = len(boxes)
    unlocked_boxes = set([0]) # Start with the first box unloked
    queue = [0] # Start exploring from the first box

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                queue.append(key)

    return len(unlocked_boxes) == total_boxes
