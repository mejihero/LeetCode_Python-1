class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n <= 2:
            return False

        while n > 3:
            if n % 3 == 0:
                n /= 3
            else:
                return False

        if n != 2:
            return True
        else:
            return False






    """
        Time Complexity = O(n)
        Space Complexity = O(1)

        Given an integer, write a function to determine if it is a power of three.

        Example:
        Input: 45
        Output: false
    """
