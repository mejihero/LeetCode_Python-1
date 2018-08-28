class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        opt_num = 0
        a = abs(x)
        while(a!=0):
            temp = a % 10
            opt_num = opt_num * 10 + temp
            a = int(a / 10)

        if x >= 0 and x == opt_num:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution().isPalindrome(0))






    """
        Time Complexity = O(log(x))
        Space Complexity = O(1)

        Determine whether an integer is a palindrome.
        An integer is a palindrome when it reads the same backward as forward.

        Example:
        Input: 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    """
