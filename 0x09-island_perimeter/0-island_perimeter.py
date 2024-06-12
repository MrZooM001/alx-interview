#!/usr/bin/python3
"""Module to implement Island Perimeter algorithm"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by a grid of 0s and 1s.

    Arguments:
        grid (List[List[int]]): A 2D list where 1 represents land
        and 0 represents water.

    Returns:
        int: The perimeter of the island.

    The function iterates through each cell in the grid.
    If a cell contains land (1), it checks the adjacent cells
    (up, down, left, right) to determine the perimeter.
    The perimeter is calculated by counting the number of
    adjacent cells that are water (0).
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
