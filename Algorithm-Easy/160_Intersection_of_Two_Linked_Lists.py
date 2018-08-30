# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB

        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next

            if not p2:
                p2 = headA
            else:
                p2 = p2.next

        return p2






    """
            Time Complexity = O(n)
            Space Complexity = O(1)


            Write a program to find the node at which the intersection of two singly linked lists begins.


            For example, the following two linked lists:

            A:          a1 → a2
                               ↘
                                 c1 → c2 → c3
                               ↗
            B:     b1 → b2 → b3
            begin to intersect at node c1.
    """
