#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """check if all the boxes can be open"""
    to_open = [0]
    open_boxes = [0]
    while len(to_open) > 0:
        box = to_open.pop(0)

        for key in boxes[box]:
            if key not in open_boxes:
                open_boxes.append(key)
                to_open.append(key)

    if len(open_boxes) == len(boxes):
        return True
    else:
        return False


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
