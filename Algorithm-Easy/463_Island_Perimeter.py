class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        p = 0
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 1:
                    p = p+4
                    if m != 0 and grid[m-1][n] == 1:
                        p = p-1
                    if m != M-1 and grid[m+1][n] == 1:
                        p = p-1
                    if n != 0 and grid[m][n-1] == 1:
                        p = p-1
                    if n != N-1 and grid[m][n+1] == 1:
                        p = p-1
        return p






    """
    You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

    The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



    Example:

    Input:
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

    Output: 16
    """
