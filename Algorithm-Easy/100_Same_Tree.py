# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False

if __name__ == "__main__":
    root1, root1.left, root1.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root2, root2.left, root2.right = TreeNode(1), TreeNode(2), TreeNode(3)
    print(Solution().isSameTree(root1, root2))






    """
            Time Complexity = O(n)
            Space Complexity = O(h) , where h means the height of binary tree

            Given two binary trees, write a function to check if they are the same or not.
            Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

            Example:
            Input:     1         1
                      / \       / \
                     2   3     2   3
                    [1,2,3],   [1,2,3]
            Output: true
    """
