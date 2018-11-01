# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0 :
            return None

        all_ls =[]
        for list in lists:
            while list:
                all_ls.append(list.val)
                list = list.next
        all_ls.sort()

        head = dumphead = ListNode(None)
        for item in all_ls:
            head.next = ListNode(item)
            head = head.next

        return dumphead.next






        """

            Output: 5
        """
