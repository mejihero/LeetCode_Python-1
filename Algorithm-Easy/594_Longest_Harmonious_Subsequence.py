class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}

        for n in nums:
            d[n] = d.get(n, 0) + 1

        res = 0
        for n in nums:
            if n - 1 in d:
                res = max(d[n - 1] + d[n], res)
        return res






        """
            We define a harmonious array is an array where the difference between its maximum value and its minimum
            value is exactly 1.

            Now, given an integer array, you need to find the length of its longest harmonious subsequence among all
            its possible subsequences.

            Example 1:

            Input: [1,3,2,2,5,2,3,7]
            Output: 5
            Explanation: The longest harmonious subsequence is [3,2,2,2,3].

            Note: The length of the input array will not exceed 20,000.
        """
