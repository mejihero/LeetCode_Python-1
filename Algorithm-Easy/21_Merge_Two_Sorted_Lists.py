# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode (1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print(Solution().mergeTwoLists(l1, l2))






    """
        Time Complexity = O(N)
        Space Complexity = O(1)

        Merge two sorted linked lists and return it as a new list.
        The new list should be made by splicing together the nodes of the first two lists.

        Example:

        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
        __repr__ should return a printable representation of the object,
        most likely one of the ways possible to create this object.
    """
