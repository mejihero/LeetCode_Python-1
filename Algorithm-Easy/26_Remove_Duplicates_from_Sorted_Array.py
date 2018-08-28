class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1

if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,2,3,6,6,9,9,11]))






    """
        Time Complexity = O(N)
        Space Complexity = O(1)

        "if not "nums": will execute if bar is any kind of zero or empty container, or False

        Given a sorted array nums, remove the duplicates in-place such that each element appear only once
        and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place
        with O(1) extra memory.

        Example:
        Given nums = [1,1,2],
        Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
        It doesn't matter what you leave beyond the returned length.
    """
