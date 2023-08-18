#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""
def join(T, R):
    res = []
    for e in R:
        res += T[e]
    return res

def canUnlockAll(boxes):
    index = 0
    total_boxes = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total_boxes[index:]):
            if j not in total_boxes:
                total_boxes.append(j)
                index = 1
                added = True

    return len(total_boxes) == len(boxes)
