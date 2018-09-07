class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lookup = []
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup.append(s[i])
        print(lookup)

        for j in range(len(t)):
            if s[j] not in lookup:
                return False

        return True

if __name__ == '__main__':
    print(Solution().isAnagram('anagram','nagaram'))






    """
        Time Complexity = O(N)
        Space Complexity = O(N)

        Given two strings s and t , write a function to determine if t is an anagram of s.

        Example:
        Input: s = "anagram", t = "nagaram"
        Output: true
    """
