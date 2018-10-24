class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sorted_num = sorted(nums,reverse=True)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(value) for value in range(4,len(nums)+1)]
        dic = dict(zip(sorted_num,rank))
        return [dic[value] for value in nums]






        """
        Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

        Example 1:
        Input: [5, 4, 3, 2, 1]
        Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
        Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
        For the left two athletes, you just need to output their relative ranks according to their scores.
        """
