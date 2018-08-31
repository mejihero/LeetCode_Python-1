class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        print(k)
        print(nums[:k])
        print(nums[len(nums)-k:])
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    print(nums)






    """
            Time Complexity = O(n)
            Space Complexity = O(1)

            Given an array, rotate the array to the right by k steps, where k is non-negative.

            Example:
            Input: [1,2,3,4,5,6,7] and k = 3
            Output: [5,6,7,1,2,3,4]
            Explanation:
            rotate 1 steps to the right: [7,1,2,3,4,5,6]
            rotate 2 steps to the right: [6,7,1,2,3,4,5]
            rotate 3 steps to the right: [5,6,7,1,2,3,4]
    """
