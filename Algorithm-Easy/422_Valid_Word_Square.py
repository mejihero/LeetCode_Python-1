class Solution:
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        m = len(words)
        if m != 0:
            n = len(words[0])
        else:
            n = 0

        if m != n:
            return False

        for x in range(m):
            n = len(words[x])
            c = 0
            #print('x', x)

            for y in range(m):
                if len(words[y]) < x + 1:
                    break
                c += 1

            if c != n:
                return False

            for y in range(n):
                if words[x][y] != words[y][x]:
                    return False

        return True






    """
        Given a sequence of words, check whether it forms a valid word square.

        A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

        Note:
        The number of words given is at least 1 and does not exceed 500.
        Word length will be at least 1 and does not exceed 500.
        Each word contains only lowercase English alphabet a-z.
        Example 1:

        Input:
        [
          "abcd",
          "bnrt",
          "crmy",
          "dtye"
        ]

        Output:
        true
    """
