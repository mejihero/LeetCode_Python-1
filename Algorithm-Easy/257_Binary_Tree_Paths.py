# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result, path = [], []
        self.binaryTreePathsRecu(root, path, result)
        return result

    def binaryTreePathsRecu(self, node, path, result):
        if node is None:
            return

        if node.left is node.right is None:
            ans = ""
            for n in path:
                ans += str(n.val) + "->"
            result.append(ans + str(node.val))

        if node.left:
            path.append(node)
            self.binaryTreePathsRecu(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathsRecu(node.right, path, result)
            path.pop()






    """
        Time Complexity = O(N * h)
        Space Complexity = O(h)

        Given a binary tree, return all root-to-leaf paths.
        Note: A leaf is a node with no children.

        Example:
        Input:
           1
         /   \
        2     3
         \
          5

        Output: ["1->2->5", "1->3"]

        Explanation: All root-to-leaf paths are: 1->2->5, 1->3
    """
