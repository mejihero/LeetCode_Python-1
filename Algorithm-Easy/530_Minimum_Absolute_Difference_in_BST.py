# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        iot_list = []
        def InOrderTraversal(node):
            if node.left:
                InOrderTraversal(node.left)
            iot_list.append(node.val)
            if node.right:
                InOrderTraversal(node.right)
            return

        InOrderTraversal(root)

        min_abs = float('inf')

        for i in range(1,len(iot_list)):
            diff = iot_list[i] - iot_list[i-1]
            if diff < min_abs:
                min_abs = diff
        return min_abs






        """
            Given a binary search tree with non-negative values, find the minimum absolute difference between
            values of any two nodes.

            Example:

            Input:

               1
                \
                 3
                /
               2

            Output:
            1

            Explanation:
            The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

        """
