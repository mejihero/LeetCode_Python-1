class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            print('mid', mid)
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == "__main__":
    print(Solution().findPeakElement([1,2,3,1]))


"""
    # nums = [1,2,3,1]
    # left - 0, right - 3, mid = 1 => nums[1] < nums[2]
    #  left = mid + 1 = 2, right - 3, mid = 2 => nums[2] > nums[3]
    # right - 2, left = 2, out of while loop, return left

            /\
          /  \/\   /\
         /      \/   \
        /             \
        从上图可以看出，一条上升的边和一条下降的边之间至少夹着一个顶点元素。由于左右两边各有一个无穷小的元素，
        所以起始的时候最左边的边是上升的，最右边的边是下降的。要求时间复杂度为log(n)，我们可以通过二分搜索来判断。
        我们取中点和它后面的一个点，如果这两个点构成的边是上升的，那我们就把中点左边的点抛弃掉，这时候仍然满足最左
        边的边是上升的，最右边的边是下降的；如果两个点构成的边是下降的，那么该把中点右边的点抛弃掉，这样仍然满足上面的要
        求，保证左右两个点之间至少有一个顶点元素。至于如何在两点中选择新的左右节点，我们要尽可能使新的左右节点靠近顶
        点元素，因为最终的终止条件是左右节点重合。所以选择新的左节点时，应该选中点的后一个节点，而选新的右节点时，选择中点。

"""
