class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        local_count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                local_count = 0
            else:
                local_count += 1
                count = local_count
        return count

if __name__ == '__main__':
    print(Solution().lengthOfLastWord("Hello World"))






    """
        Time Complexity = O(N)
        Space Complexity = O(1)

        Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
        return the length of last word in the string.
        If the last word does not exist, return 0.
        Note: A word is defined as a character sequence consists of non-space characters only.

        Example:
        Input: "Hello World"
        Output: 5
    """
