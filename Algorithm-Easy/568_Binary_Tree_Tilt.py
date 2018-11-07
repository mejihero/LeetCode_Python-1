# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def subTreeSum(root):
            if not root: return 0
            lsum = subTreeSum(root.left)
            rsum = subTreeSum(root.right)
            self.ans += abs(lsum - rsum)
            return root.val + lsum + rsum

        subTreeSum(root)

        return self.ans






    """
        The tilt of the whole tree is defined as the sum of all nodes' tilt.

        Example:

        Input:
                 1
               /   \
              2     3
        Output: 1
        Explanation:
        Tilt of node 2 : 0
        Tilt of node 3 : 0
        Tilt of node 1 : |2-3| = 1
        Tilt of binary tree : 0 + 0 + 1 = 1

        Note:

            The sum of node values in any subtree won't exceed the range of 32-bit integer.
            All the tilt values won't exceed the range of 32-bit integer.

    """
