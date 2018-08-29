# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_height(root):
            if root is None:
                return 0
            left_height, right_height = get_height(root.left), get_height(root.right)
            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return (get_height(root) >= 0)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(15)
    print(Solution().levelOrderBottom(root))






    """
            Time Complexity = O(n)
            Space Complexity = O(h)

            Given a binary tree, determine if it is height-balanced.
            For this problem, a height-balanced binary tree is defined as:
            A binary tree in which the depth of the two subtrees of every node never differ by more than 1.

            Example:
            Given binary tree [3,9,20,null,null,15,7],

                    3
                   / \
                  9  20
                    /  \
                   15   7
            Return true.
    """
