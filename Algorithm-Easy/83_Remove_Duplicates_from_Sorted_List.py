# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        dummy = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head

if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    print(head)
    print(Solution().deleteDuplicates(head))






    """
            Time Complexity = O(n)
            Space Complexity = O(1)

            Given a sorted linked list, delete all duplicates such that each element appear only once.

            Example:
            Input: 1->1->2->3->3
            Output: 1->2->3
    """
