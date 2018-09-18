class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 0:
            return 0
        else:
            output = (num - 1) % 9 + 1

        return output






    """
        Time Complexity = O(1)
        Space Complexity = O(1)

        Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

        Example:
        Input: 38
        Output: 2
        Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
                     Since 2 has only one digit, return it.

        Explanation:
        根据提示，当输入从1到100变化时，可以发现，输出在“1，2，3，4，5，6，7，8，9，1，2，3，4，5，6，7，8，9，…”这样循环。
        于是，就有了下面O(1)的算法。 
        dr(n) = 0, if n = 0
        dr(n) = 9, if n != 0 and n mod 9 == 0
        dr(n) = n mod 9, if n mod 9 != 0
        或，
        dr(n) = 1 + (n-1) mod 9

        这个问题又叫做“digit root”问题，参看：
        https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
    """
