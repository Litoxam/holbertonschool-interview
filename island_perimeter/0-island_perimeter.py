#!/usr/bin/python3
"""
Module that contains a function to calculate
the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Return the perimeter of the island described in the grid.
    """

    perimeter = 0

    # Go through every cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            # Only process land cells
            if grid[row][col] == 1:

                # A single land cell has 4 sides
                perimeter += 4

                # If there is land above, remove the shared edge
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                # If there is land on the left, remove the shared edge
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
