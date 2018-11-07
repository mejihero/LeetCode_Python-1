class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        minn = minn2 = float('inf')
        maxx = maxx2 = -float('inf')

        for i, arr in enumerate(arrays):
            if arr[-1] > maxx:
                maxx2 = maxx
                maxx = arr[-1]
                i_max = i
            elif arr[-1] > maxx2:
                maxx2 = arr[-1]
            if arr[0] < minn:
                minn2 = minn
                minn = arr[0]
                i_min = i
            elif arr[0] < minn2:
                minn2 = arr[0]

        if i_max != i_min:
            return maxx - minn
        if (maxx - minn2) > (maxx2 - minn):
            return maxx - minn2
        else:
            return maxx2 - minn






    """
         Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two
         different arrays (each array picks one) and calculate the distance. We define the distance between two
         integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

        Example 1:

        Input:
        [[1,2,3],
         [4,5],
         [1,2,3]]
        Output: 4
        Explanation:
        One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

        Note:

            Each given array will have at least 1 number. There will be at least two non-empty arrays.
            The total number of the integers in all the m arrays will be in the range of [2, 10000].
            The integers in the m arrays will be in the range of [-10000, 10000].

    """
