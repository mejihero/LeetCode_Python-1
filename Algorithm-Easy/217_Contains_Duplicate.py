class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

if __name__ == '__main__':
    print(Solution().containsDuplicate([1,1,2,3,5,6]))






        """

            Time Complexity = O(n)
            Space Complexity = O(n)

            Given an array of integers, find if the array contains any duplicates.
            Your function should return true if any value appears at least twice in
            the array, and it should return false if every element is distinct..

            Example:
            Input: [1,1,1,3,3,4,3,2,4,2]
            Output: true
        """
