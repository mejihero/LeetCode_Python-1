class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(v % 2 for v in collections.Counter(s).values()) < 2






    """
        Time Complexity = O(n)
        Space Complexity = O(1)

        Given a string, determine if a permutation of the string could form a palindrome.

        Example:
        Input: "carerac"
        Output: true
    """
