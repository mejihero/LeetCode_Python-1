class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k

        # for the first 2 posts
        sameColor = k
        diffColor = k * (k - 1)

        for i in range(2, n):
            temp = diffColor
            diffColor = (sameColor + diffColor) * (k - 1)
            sameColor = temp

        return sameColor + diffColor






    """
        Time Complexity = O(n)
        Space Complexity = O(1)

        There is a fence with n posts, each post can be painted with one of the k colors.
        You have to paint all the posts such that no more than two adjacent fence posts have the same color.
        Return the total number of ways you can paint the fence.

        Note:
        n and k are non-negative integers..

        Example:
        Input: n = 3, k = 2
        Output: 6
        Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

                    post1  post2  post3
         -----      -----  -----  -----
           1         c1     c1     c2
           2         c1     c2     c1
           3         c1     c2     c2
           4         c2     c1     c1
           5         c2     c1     c2
           6         c2     c2     c1

         Explanation:
         n是有几个标杆，k是有几种颜色
            1. n == 0，当没有标杆的时候，就没有任何粉刷的可能。
            2. n == 1，当只有一根标杆的时候，那就是有几种颜料就又几种粉刷的可能性。
            3. 当n >= 2的时候。因为题目条件是最多两个相邻的标杆能够颜色相同，可能性就只有两种，一种是两根标杆的颜色相同，
            另一种就是两根标杆的颜色不同。开始两根标杆的颜色相同的可能性就是颜色的可能性，即k。

            sameColor = k
            如果是颜色不同的可能性，那么就是k颜色中选一种，第二根剩下的颜色中选一个种，即k-1。所以根据概率论来说，就是k*（k-1）。

            diffColor = k * (k - 1)

            4. 对于新的一根标杆。参考n=2的时候，相同颜色sameColor的可能性，就是之前的不同颜色diffColor的可能性数量，
            因为根据题意，只有不同颜色，第三根才可能是相同颜色。而新标杆的不同颜色diffColor的可能性，因为第二根标杆已经有了颜色，
            但是不论是什么颜色，我们都可以给一个不同的颜色，所以就是k-1种可能，即（sameColor + diffColor）*（k-1）。

            for i in range(2, n):
                        temp = diffColor
                        diffColor = (sameColor + diffColor) * (k - 1)
                        sameColor = temp

            5. 根据推论4，只要循环到所有标杆，得到的sameColor + diffColor就是我们要的结果。
    """
