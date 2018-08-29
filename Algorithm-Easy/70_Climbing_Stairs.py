class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current

if __name__ == '__main__':
    print(Solution().climbStairs(2))






    """
            Time Complexity = O(n)
            Space Complexity = O(1)

            You are climbing a stair case. It takes n steps to reach to the top.
            Each time you can either climb 1 or 2 steps. In how many distinct ways can
            you climb to the top?
            Note: Given n will be a positive integer.

            Example:
            Input: 3
            Output: 3
            Explanation: There are three ways to climb to the top.
            1. 1 step + 1 step + 1 step
            2. 1 step + 2 steps
            3. 2 steps + 1 step

            斐波那契数列（Fibonacci sequence）

    """
