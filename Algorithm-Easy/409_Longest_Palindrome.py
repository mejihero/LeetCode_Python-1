class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = dict()

        for i in s:
            if i in map.keys():
                map[i] += 1
            else:
                map[i] = 1

        # compute the length
        mark = 0
        len = 0
        for j in map.keys():
            if map[j]%2 == 1:
                mark += 1
            len += map[j]//2

        len = len * 2 + 1 if mark > 0 else len * 2

        return len if len > 0 else (1 if mark > 0 else 0)







    """
        Given a string which consists of lowercase or uppercase letters, find the length of
        the longest palindromes that can be built with those letters.

        This is case sensitive, for example "Aa" is not considered a palindrome here.

        Note:
        Assume the length of given string will not exceed 1,010.

        Example:

        Input:
        "abccccdd"

        Output:
        7
    """
