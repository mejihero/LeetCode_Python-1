# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(float("-inf"))
        dummy.next = head
        previous, current = dummy, dummy.next

        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current

            current = current.next

        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print(Solution().removeElements(head, 6))






        """

            Time Complexity = O(n)
            Space Complexity = O(1)

            Remove all elements from a linked list of integers that have value val.

            Example:
            Input:  1->2->6->3->4->5->6, val = 6
            Output: 1->2->3->4->5
        """
