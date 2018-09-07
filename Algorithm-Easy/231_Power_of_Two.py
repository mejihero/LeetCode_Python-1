class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n-1)) == 0

class Solution2:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        while n%2 == 0:
            n /= 2
        return True if n==1 else False

if __name__ == '__main__':
    print(Solution().isPowerOfTwo(5))






        """

            Time Complexity = O(log(n)) or O(1)
            Space Complexity = O(1)

            Given an integer, write a function to determine if it is a power of two.

            Example:
            Input: 1
            Output: true
            Explanation: 20 = 1
        """
