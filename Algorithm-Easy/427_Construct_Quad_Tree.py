"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        self.grid = grid
        return self.createTree(len(grid), 0, 0)

    def createTree(self, size, x, y):
        for i in range(x, x + size):
            for j in range(y, y + size):
                if self.grid[i][j] != self.grid[x][y]:
                    halfSize = size // 2
                    return Node(
                        True,
                        False,
                        self.createTree(halfSize, x, y),
                        self.createTree(halfSize, x, y + halfSize),
                        self.createTree(halfSize, x + halfSize, y),
                        self.createTree(halfSize, x + halfSize, y + halfSize),
                    )

        return Node(self.grid[x][y] == 1, True, None, None, None, None)






    """
        We want to use quad trees to store an N x N boolean grid. Each cell in
        the grid can only be true or false. The root node represents the whole
        grid. For each node, it will be subdivided into four children nodes until
        the values in the region it represents are all the same.

        Each node has another two boolean attributes : isLeaf and val. isLeaf is
        true if and only if the node is a leaf node. The val attribute for a leaf
        node contains the value of the region it represents.

        Reference: https://blog.csdn.net/fuxuemingzhu/article/details/81836838
    """
