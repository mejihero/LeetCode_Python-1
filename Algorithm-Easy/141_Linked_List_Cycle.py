# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print(Solution().hasCycle(head))






    """
            Time Complexity = O(n)
            Space Complexity = O(1)

            快慢指针技巧，slow指针和fast指针开始同时指向头结点head，fast每次走两步，slow每次走一步。
            如果链表不存在环，那么fast或者fast.next会先到None。如果链表中存在环路，则由于fast指针
            移动的速度是slow指针移动速度的两倍，所以在进入环路以后，两个指针迟早会相遇，
            如果在某一时刻slow==fast，说明链表存在环路。

            Given a linked list, determine if it has a cycle in it.

            Follow up:
            Can you solve it without using extra space?
    """
