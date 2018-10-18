"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        cur = [root]
        nex = []
        ans=[]
        while cur:
            tmp = []
            for n in cur:
                tmp.append(n.val)
                for c in n.children:
                    nex.append(c)
            ans.append(tmp)
            cur = nex
            nex = []

        return ans






    """
        Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

        For example, given a 3-ary tree:
                    1
                  / | \
                 3  2  4
                / \
               5   6

        We should return its level order traversal:

        [
             [1],
             [3,2,4],
             [5,6]
        ]


        Note:

        The depth of the tree is at most 1000.
        The total number of nodes is at most 5000.
    """
