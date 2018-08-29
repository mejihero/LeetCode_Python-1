class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1


if __name__ == "__main__":
    print(Solution().mySqrt(11))






    """
        Time Complexity = O(log(N))
        Space Complexity = O(1)

        Implement int sqrt(int x).
        Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
        Since the return type is an integer, the decimal digits are truncated and only the integer part
        of the result is returned.

        Example:
        Input: 8
        Output: 2
        Explanation: The square root of 8 is 2.82842..., and since
                     the decimal part is truncated, 2 is returned.
    """
