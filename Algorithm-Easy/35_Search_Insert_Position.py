class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums) - 1]:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] >= target:
                return i


if __name__ == '__main__':
    print(Solution().searchInsert([1,2,3], 6))






    """
        Time Complexity = O(N)
        Space Complexity = O(1)
        What if we want Time Complexity = O(logn)
        https://github.com/kamyu104/LeetCode/blob/master/Python/search-insert-position.py

        Given a sorted array and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.
        You may assume no duplicates in the array.

        Example:
        Input: [1,3,5,6], 5
        Output: 2
    """
