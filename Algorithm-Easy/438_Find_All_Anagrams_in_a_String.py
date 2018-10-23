class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s = list(s)
        ans = []

        #make hashmap of chars and freqs in p
        p_dict = {}
        for c in p:
            if c not in p_dict:
                p_dict[c] = 1
            else:
                p_dict[c] += 1

        begin = 0
        end = 0
        counter = len(p_dict)
        while end < len(s):
            end_char = s[end]

            if end_char in p_dict:
                p_dict[end_char] -= 1
                if p_dict[end_char] == 0:
                    counter -= 1

            end += 1

            while counter == 0:
                if end - begin == len(p):
                    ans.append(begin)

                if s[begin] in p_dict:
                    p_dict[s[begin]] += 1
                    if p_dict[s[begin]] > 0:
                        counter += 1

                begin += 1

        return ans






    """
        Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

        Strings consists of lowercase English letters only and the length of both strings s and p will
        not be larger than 20,100.

        The order of output does not matter.

        Example 1:

        Input:
        s: "cbaebabacd" p: "abc"

        Output:
        [0, 6]

        Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".
    """
