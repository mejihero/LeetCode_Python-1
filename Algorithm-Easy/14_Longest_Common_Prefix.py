class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["hello", "heaven", "heavy"]))






    """
        Time Complexity = O(N*k), k is the length of the common prefix
        Space Complexity = O(1)

        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".

        Example :
        Input: ["flower","flow","flight"]
        Output: "fl"
    """
