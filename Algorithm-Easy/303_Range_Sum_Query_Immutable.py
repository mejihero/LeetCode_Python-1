class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums:
            self.accu.append(self.accu[-1] + num),

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)






    """
        Time Complexity = O(n)
        Space Complexity = O(n)

        Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

        Example:
        Given nums = [-2, 0, 3, -5, 2, -1]

        sumRange(0, 2) -> 1
        sumRange(2, 5) -> -1
        sumRange(0, 5) -> -3

        Explaination:
        在初始化的时候，将从第一个元素开始到当前位置的所有元素的和求出来，存放到数组sums中。那么每次求一个范围的和时，只要计算两个下标处和的差即可。
    """
