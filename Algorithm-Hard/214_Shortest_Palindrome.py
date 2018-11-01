class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        t = s[::-1]
        for i in range(n,-1,-1):
            print(s[:i], t[n-i:])
            print(i)
            if s[:i] == t[n-i:]:
                break
        return t[:n-i] + s

if __name__ == "__main__":
    print(Solution().shortestPalindrome("abcd"))






    """
        Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

        Example 1:

        Input: "aacecaaa"
        Output: "aaacecaaa"

        Example 2:

        Input: "abcd"
        Output: "dcbabcd"
    """
