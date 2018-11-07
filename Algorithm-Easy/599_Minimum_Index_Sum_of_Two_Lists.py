class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {rest : i for i, rest in enumerate(list1)}
        dict2 = {rest : i for i, rest in enumerate(list2)}
        dictSum = {rest : dict1[rest]+dict2[rest] for rest in dict1 if rest in dict2}
        minSum = min(dictSum.values())
        return [key for key in dictSum if dictSum[key] == minSum]






        """
            Time Complexity = O(N*k), where k is the length of needle
            Space Complexity = O(k)
            Less Complexity?
            https://github.com/kamyu104/LeetCode/blob/master/Python/implement-strstr.py

            Implement strStr().
            Return the index of the first occurrence of needle in haystack,
            or -1 if needle is not part of haystack.

            Example:
            Input: haystack = "hello", needle = "ll"
            Output: 2
        """
