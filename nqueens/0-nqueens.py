#!/usr/bin/python3
"""
Solve the N Queens puzzle using backtracking.
"""

import sys


# Check the number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Check if N is a number
if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

# Convert N to an integer
size = int(sys.argv[1])

# Check if N is at least 4
if size < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(queens, row, col):
    """
    Check if a queen can be placed at (row, col).
    """

    # Check every queen already placed
    for previous_row in range(row):
        previous_col = queens[previous_row]

        # Same column
        if previous_col == col:
            return False

        # Same diagonal
        if abs(previous_col - col) == abs(previous_row - row):
            return False

    return True


def solve(queens, row):
    """
    Try to place a queen on each row.
    """

    # If all queens are placed, print the solution
    if row == size:
        solution = []

        for current_row in range(size):
            solution.append([current_row, queens[current_row]])

        print(solution)
        return

    # Try every column in the current row
    for col in range(size):

        # Place the queen only if the position is safe
        if is_safe(queens, row, col):

            # Place the queen
            queens[row] = col

            # Move to the next row
            solve(queens, row + 1)

            # Remove the queen to try another position
            queens[row] = -1


# queens[row] = column where the queen is placed
queens = [-1] * size

# Start solving from the first row
solve(queens, 0)
