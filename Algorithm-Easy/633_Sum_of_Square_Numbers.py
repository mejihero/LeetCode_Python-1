class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        st = 0
        ed = int(math.sqrt(c))

        while st <= ed:
            total = st*st +ed*ed
            if total > c:
                ed -= 1;
            elif total < c:
                st += 1
            else:
                return True
        return False






    """
        Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

        Example 1:

        Input: 5
        Output: True
        Explanation: 1 * 1 + 2 * 2 = 5

        Example 2:

        Input: 3
        Output: False

    """
