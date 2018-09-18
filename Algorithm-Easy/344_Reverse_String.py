class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        i, j = 0, len(string) - 1
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return "".join(string)






    """
        Time Complexity = O(n)
        Space Complexity = O(n)

        Write a function that takes a string as input and returns the string reversed.

        Example:
        Input: "A man, a plan, a canal: Panama"
        Output: "amanaP :lanac a ,nalp a ,nam A"
    """
