class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    print(Solution().strStr("hello", "lo"))






    """
        Time Complexity = O(N*k), where k is the length of needle
        Space Complexity = O(k)
        Less Complexity?
        https://github.com/kamyu104/LeetCode/blob/master/Python/implement-strstr.py

        Implement strStr().
        Return the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack.

        Example:
        Input: haystack = "hello", needle = "ll"
        Output: 2
    """
