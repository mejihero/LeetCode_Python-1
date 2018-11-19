# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, float('-inf'), float('inf'))



    def valid(self, root, min, max):
        if not root:
            return True

        if root.val >= max or root.val <= min:
            return False

        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)






    """
        Given a binary tree, determine if it is a valid binary search tree (BST).

        Assume a BST is defined as follows:

            The left subtree of a node contains only nodes with keys less than the node's key.
            The right subtree of a node contains only nodes with keys greater than the node's key.
            Both the left and right subtrees must also be binary search trees.

        Example:

        Input:
                2
               / \
              1   3
        Output: true

    """
