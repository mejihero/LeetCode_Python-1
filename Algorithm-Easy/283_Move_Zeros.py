class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0

if __name__ == '__main__':
    s = Solution()
    r = s.moveZeroes([0, 1, 0, 3, 12])
    print(r)






    """
        Time Complexity = O(n)
        Space Complexity = O(1)

        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative
        order of the non-zero elements.

        Example:
        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
    """
