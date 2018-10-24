# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        count = collections.defaultdict(int)

        def preorder(root):
            if root:
                count[root.val] += 1
                preorder(root.left)
                preorder(root.right)

        preorder(root)

        max_occ = max(count.values())

        return [k for k in count if count[k] == max_occ]






        """
        Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

        Assume a BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than or equal to the node's key.
        The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
        Both the left and right subtrees must also be binary search trees.


        For example:
        Given BST [1,null,2,2],

        1
        \
         2
        /
        2


        return [2].
        """
