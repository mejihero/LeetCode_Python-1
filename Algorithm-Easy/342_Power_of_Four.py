class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num >= 4:
            if num % 4 == 0:
                num /= 4
            else:
                return False

        if num == 1:
            return True
        else:
            return False






    """
        Time Complexity = O(n)
        Space Complexity = O(1)

        Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

        Example:
        Input: 16
        Output: true
    """
