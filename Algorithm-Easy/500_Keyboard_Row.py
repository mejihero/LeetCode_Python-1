class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
         # initialize the three rows of a keyboard
        top = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        middle = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        bottom = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        # put the rows in a list
        rows = [top, middle, bottom]
        # initialize an empty list for the output
        output = []

        # iterate through the input list
        for word in words:
            # find which row the first character is in
            for row in rows:
                if word[0].lower() in row:
                    result_row = row
                    break
            # check if the rest of the character is in the same row
            for char in word:
                j = 0
                # indicate if a character is not in the same row
                if char.lower() not in result_row:
                    j = -1
                    break
            # if all characters are in the same row, add the word to the output list
            if j != -1:
                output.append(word)
        # return the output list
        return output






        """
        Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

        Example:

        Input: ["Hello", "Alaska", "Dad", "Peace"]
        Output: ["Alaska", "Dad"]
        """
