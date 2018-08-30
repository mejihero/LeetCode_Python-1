class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans

if __name__ == '__main__':
    print(Solution().singleNumber([1, 1, 2, 2, 3]))






    """
            Time Complexity = O(n)
            Space Complexity = O(1)


            Given a non-empty array of integers, every element appears twice except for one. Find that single one.
            Note:
            Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

            Example:
            Input: [4,1,2,1,2]
            Output: 4

            对数组元素执行异或运算，最终结果即为所求。
            由于异或运算的性质，两个相同数字的亦或等于0，而任意数字与0的亦或都等于它本身。另外，异或运算满足交换律。
            a ^ b = (a & !b) || (!a & b)
    """
