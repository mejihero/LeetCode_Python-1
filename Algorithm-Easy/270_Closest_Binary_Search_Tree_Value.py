# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        gap = float("inf")
        closest = float("inf")

        while root:
            if abs(root.val - target) < gap:
                gap = abs(root.val - target)
                closest = root

            if target == root.val:
                break
            elif target < root.val:
                root = root.left
            else:
                root = root.right

        return closest.val






    """
        Time Complexity = O(h)
        Space Complexity = O(1)

        Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

        Note:
        Given target value is a floating point.
        You are guaranteed to have only one unique value in the BST that is closest to the target.

        Example:
        Input: root = [4,2,5,1,3], target = 3.714286
                4
               / \
              2   5
             / \
            1   3

            Output: 4
    """
