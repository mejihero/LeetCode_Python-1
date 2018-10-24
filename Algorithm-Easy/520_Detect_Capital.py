class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cap = 0
        for char in word:
            if char.isupper():
                cap += 1

        if cap == 1 and word[0].isupper():
            return True
        elif cap == len(word):
            return True
        elif cap == 0:
            return True
        else:
            return False






            """
            Given a word, you need to judge whether the usage of capitals in it is right or not.

            We define the usage of capitals in a word to be right when one of the following cases holds:

            All letters in this word are capitals, like "USA".
            All letters in this word are not capitals, like "leetcode".
            Only the first letter in this word is capital if it has more than one letter, like "Google".
            Otherwise, we define that this word doesn't use capitals in a right way.
            Example 1:
            Input: "USA"
            Output: True
            Example 2:
            Input: "FlaG"
            Output: False
            Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
            """
