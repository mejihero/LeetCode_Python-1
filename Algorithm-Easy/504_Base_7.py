class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = abs(num)
        ans = ''
        while n:
            ans += str(n % 7)
            n //= 7
        return ['', '-'][num < 0] + ans[::-1] or '0'






        """
        Given an integer, return its base 7 string representation.

        Example 1:
        Input: 100
        Output: "202"
        Example 2:
        Input: -7
        Output: "-10"
        Note: The input will be in range of [-1e7, 1e7].
        """
