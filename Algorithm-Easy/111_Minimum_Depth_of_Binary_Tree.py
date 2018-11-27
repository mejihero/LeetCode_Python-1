# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(15)
    print(Solution().minDepth(root))






    """
            Time Complexity = O(n)
            Space Complexity = O(h)


            Given a binary tree, find its minimum depth.
            The minimum depth is the number of nodes along the shortest path from the root
            node down to the nearest leaf node.
            Note: A leaf is a node with no children.

            Example:
            Given binary tree [3,9,20,null,null,15,7],

                    3
                     \
                     20
                    /  \
                   15   7
            Return its minimum depth = 2.
    """
