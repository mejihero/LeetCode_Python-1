class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1

        for i in range(1, len(nums)):
            print ('nums[idx], cnt', nums[idx], cnt)
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1

        return nums[idx]

if __name__ == "__main__":
    #print(Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]))
    #print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(Solution().majorityElement([5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 5]))






    """
            Time Complexity = O(n)
            Space Complexity = O(1)

            Given an array of size n, find the majority element. The majority element is the element that appears
            more than ⌊ n/2 ⌋ times.
            You may assume that the array is non-empty and the majority element always exist in the array.

            Example:
            Input: [2,2,1,1,1,2,2]
            Output: 2
    """
