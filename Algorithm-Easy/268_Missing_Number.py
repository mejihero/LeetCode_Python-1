class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] != i :
                return i
            else:
                i += 1
        return i

class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_sum = len(nums)*(len(nums)+1)/2
        t_sum = sum(nums)
        return int(temp_sum - t_sum)






    """
        Time Complexity = O(nlogn)
        Space Complexity = O(1)

        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

        Example:
        Input: [9,6,4,2,3,5,7,0,1]
        Output: 8

        Explaination:
        但是很明显有排序在，时间复杂度为O（nlogn），leetcode给的提示是math和bit计算，继续再考虑。
        math是说用数学方法，由于是0-n个数字，我们可以轻易的用等差数列求和公式求出和，那么减去给定数组的和，得到的结果就是缺失的数字。
    """
