class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sz_array = len(nums) + 1
        a = set([i for i in range(1, sz_array)])
        b = set(nums)
        return list(a-b)






        """
        Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

        Find all the elements of [1, n] inclusive that do not appear in this array.

        Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

        Example:

        Input:
        [4,3,2,7,8,2,3,1]

        Output:
        [5,6]
        """
