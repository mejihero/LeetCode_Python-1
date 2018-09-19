class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        lookup = collections.defaultdict(int)
        for i in nums1:
            lookup[i] += 1

        res = []
        for i in nums2:
            if lookup[i] > 0:
                res += i,
                lookup[i] -= 1
        return res






    """
        Time Complexity = O(m+n)
        Space Complexity = O(min(m,n))

        Given two arrays, write a function to compute their intersection.

        Example:
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]
    """
