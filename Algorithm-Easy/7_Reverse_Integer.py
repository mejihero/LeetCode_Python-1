class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        a = abs(x)
        while(a != 0):
            pop = a % 10
            num = num * 10 + pop
            a = int(a / 10)

        if x > 0 and num < 2147483647:
            return num
        elif x < 0 and num <= 2147483647:
            return -num
        else:
            return 0

if __name__ == '__main__':
    print(Solution().reverse(-2147483648))






    """
        Time Complexity = O(log(x))
        Space Complexity = O(1)

        Given a 32-bit signed integer, reverse digits of an integer.

        Example:
        Input: -123
        Output: -321    
    """
