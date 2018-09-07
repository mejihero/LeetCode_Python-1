class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist = float("inf")
        i, index1, index2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))

            i += 1

        return dist






    """
        Time Complexity = O(n)
        Space Complexity = O(1)

        Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

        Example:
        Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
        Input: word1 = “coding”, word2 = “practice”
        Output: 3
    """
