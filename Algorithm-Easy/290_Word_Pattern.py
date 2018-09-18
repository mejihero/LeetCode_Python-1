class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')

        if len(words) != len(pattern):
            return False

        hashmap = {}
        mapval = {}

        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in mapval:
                    return False
                hashmap[pattern[i]] = words[i]
                mapval[words[i]] = True
        return True






    """
        Time Complexity = O(n)
        Space Complexity = O(c), c stands for unique count of pattern

        Given a pattern and a string str, find if str follows the same pattern.
        Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

        Example:
        Input: pattern = "abba", str = "dog cat cat dog"
        Output: true
    """
