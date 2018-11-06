class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ''
        round = int(math.ceil(len(s) / (2.0 * k)))
        for x in range(round):
            ans += s[x * 2 * k : (x * 2 + 1) * k][::-1]
            ans += s[(x * 2 + 1) * k : (x * 2 + 2) * k]
        return ans







    """
        Given a string and an integer k, you need to reverse the first k characters for every 2k
        characters counting from the start of the string. If there are less than k characters
        left, reverse all of them. If there are less than 2k but greater than or equal to k
        characters, then reverse the first k characters and left the other as original.
        
        Example:
        Input: s = "abcdefg", k = 2
        Output: "bacdfeg"
        Restrictions:
        The string consists of lower English letters only.
        Length of the given string and k will in the range [1, 10000]
    """
