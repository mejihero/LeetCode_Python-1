# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        que = [root]

        while que:
            ans.append(1.0 * sum([n.val for n in que]) / len(que))
            nque = []
            for n in que:
                if n.left: nque.append(n.left)
                if n.right: nque.append(n.right)
            que = nque
        return ans






    """
        Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

        Example 1:

        Input:
            3
           / \
          9  20
            /  \
           15   7
        Output: [3, 14.5, 11]
        Explanation:
        The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

        Note:

            The range of node's value is in the range of 32-bit signed integer.

    """
