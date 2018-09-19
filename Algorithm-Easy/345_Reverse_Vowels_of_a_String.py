vowels = "aeiou"
        string = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if string[i].lower() not in vowels:
                i += 1
            elif string[j].lower() not in vowels:
                j -= 1
            else:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
        return "".join(string)






    """
        Time Complexity = O(n)
        Space Complexity = O(1)

        Write a function that takes a string as input and reverse only the vowels of a string.

        Example:
        Input: "leetcode"
        Output: "leotcede"
    """
