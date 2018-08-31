class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            result *= 26
            print(s[i])
            result += ord(s[i]) - ord('A') + 1
            print(result)
        return result

if __name__ == "__main__":
    print(Solution().titleToNumber("AAAB"))






    """
            Time Complexity = O(n)
            Space Complexity = O(1)

            Given a column title as appear in an Excel sheet, return its corresponding column number.
            For example:
            A -> 1
            B -> 2
            C -> 3
            ...
            Z -> 26
            AA -> 27
            AB -> 28
            ...

            Example:
            Input: "AB"
            Output: 28
    """
