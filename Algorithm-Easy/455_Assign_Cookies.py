class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        cnt = 0
        i, j = len(g) - 1, len(s) - 1
        g, s = sorted(g), sorted(s)
        while min(i, j) >= 0:
            if g[i] <= s[j]:
                cnt += 1
                j -= 1
            i -= 1
        return cnt






        """
            Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

            Please note that the string does not contain any non-printable characters.

            Example:

            Input: "Hello, my name is John"
            Output: 5

            首先对贪婪系数g、饼干尺寸s从小到大排序

            令指针i指向g的末尾，指针j指向s的末尾

            当g和s均≥0时，执行循环：

              若g[i] ≤ s[j] 则令计数器+1，并令j -= 1 （将j号饼干分配给i号孩子，并令j指向下一个更小的饼干）

              令i -= 1 （将i指向下一个贪婪系数更小的孩子）
            Reference: http://bookshadow.com/weblog/2016/11/13/leetcode-assign-cookies/
        """
