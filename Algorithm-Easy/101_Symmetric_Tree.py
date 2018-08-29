# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True

        return self.isSymmetricRecu(root.left, root.right)

    def isSymmetricRecu(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(2)
    root.left.left, root.right.right = TreeNode(3), TreeNode(3)
    root.left.right, root.right.left = TreeNode(4), TreeNode(4)
    print(Solution().isSymmetric(root))






    """
            Time Complexity = O(n), Because we traverse the entire input tree once, the total run time is O(n),
            where n is the total number of nodes in the tree.
            Space Complexity = O(h) , where h means the height of binary tree. The number of recursive calls is
            bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n).

            Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

            Example:
            This binary tree [1,2,2,3,4,4,3] is symmetric:
                1
               / \
              2   2
             / \ / \
            3  4 4  3
    """
