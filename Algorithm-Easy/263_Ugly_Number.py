class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        for i in [2,3,5]:
            while num%i == 0:
                num /= i

        return num == 1






    """
        Time Complexity = O(logn) = O(1)
        Space Complexity = O(1)

        Write a program to check whether a given number is an ugly number.
        Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

        Example:
        Input: 14
        Output: false
        Explanation: 14 is not ugly since it includes another prime factor 7.
    """
