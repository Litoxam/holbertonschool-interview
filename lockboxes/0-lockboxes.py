#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """check if all the boxes can be open"""

    if len(boxes) <= 0:
        return True

    open_boxes = {0}
    keys = [0]
    while len(keys) > 0:
        actual_box = keys.pop()

        for i in boxes[actual_box]:
            if i < len(boxes) and i not in open_boxes:
                open_boxes.add(i)
                keys.append(i)

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
