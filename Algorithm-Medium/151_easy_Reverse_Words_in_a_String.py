class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "": return s
        ls = s.split()
        print(ls)

        if ls ==[]: return ""

        ns = ""
        print(len(ls))
        for i in range(0,len(ls)-1):
            ns+=ls[len(ls)-1-i]+" "
        print(ns)
        ns+=ls[0]
        return ns

if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))






    """
        Given an input string, reverse the string word by word.

        Example:

        Input: "the sky is blue",
        Output: "blue is sky the".

        Note:

            A word is defined as a sequence of non-space characters.
            Input string may contain leading or trailing spaces. However, your reversed string should not
            contain leading or trailing spaces.
            You need to reduce multiple spaces between two words to a single space in the reversed string.

        Follow up: For C programmers, try to solve it in-place in O(1) space.

    """
