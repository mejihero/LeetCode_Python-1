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
            这道题还有一种特别巧妙的方法，虽然题目中强调了链表中不存在环，但是我们可以用环的思想来做，
            我们让两条链表分别从各自的开头开始往后遍历，当其中一条遍历到末尾时，我们跳到另一个条链表的
            开头继续遍历。两个指针最终会相等，而且只有两种情况，一种情况是在交点处相遇，另一种情况是在各
            自的末尾的空节点处相等。为什么一定会相等呢，因为两个指针走过的路程相同，是两个链表的长度之和，
            所以一定会相等。这个思路真的很巧妙，而且更重要的是代码写起来特别的简洁

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
